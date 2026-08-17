#!/usr/bin/env python3
"""Deriva métricas e hashes dos cards canônicos sem confiar em flags manuais."""
from __future__ import annotations
import hashlib, json, re, unicodedata
from copy import deepcopy
from pathlib import Path
from typing import Any
CLOZE_RE=re.compile(r"\{\{c(\d+)::([^}:]+)(?:::[^}]*)?}}",re.I|re.S); ACTIVE_SOURCES={"authored","io"}
LEARNING_FIELDS={"card_key","concept_id","tier","source","text","extra","e1_anchor","retrieval_target","semantic_review","authored_quality","cue_quality","three_word_cloze_reason","compound_answer_reason","derivation_rationale","memory_gain","ablation_loss","why_not_e1_only","confusion_target","prompt","answers","mode","masks","pair_rationale","source_credit","cognitive_purpose","visual_review","visual_evidence","image_path"}
def canonical_json(value:Any)->str:return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"))
def sha256_obj(value:Any)->str:return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()
def _plain(text:str)->str:return re.sub(r"<[^>]+>"," ",text or "")
def words(text:str)->list[str]:return [i for i in re.split(r"\s+",_plain(text).strip()) if i]
def normalized(text:str)->str:
 text=unicodedata.normalize("NFKD",_plain(text)).casefold(); text="".join(ch for ch in text if not unicodedata.combining(ch)); return re.sub(r"[^a-z0-9]+"," ",text).strip()
def learning_payload(card:dict[str,Any])->dict[str,Any]:
 payload={k:deepcopy(card[k]) for k in sorted(LEARNING_FIELDS) if k in card}; payload["source"]=str(payload.get("source") or "").lower(); payload["tier"]=str(payload.get("tier") or "nucleo").lower(); return payload
def content_sha256(card:dict[str,Any])->str:return sha256_obj(learning_payload(card))
def ordered_card_set_sha256(cards:list[dict[str,Any]])->str:return sha256_obj([{"card_key":str(c.get("card_key") or ""),"content_sha256":content_sha256(c)} for c in cards])
def derived(card:dict[str,Any])->dict[str,Any]:
 text=str(card.get("text") or ""); extra=str(card.get("extra") or ""); matches=list(CLOZE_RE.finditer(text)); answers=[m.group(2).strip() for m in matches]; visible=CLOZE_RE.sub(" ",text)
 return {"cloze_occurrences":len(matches),"cloze_indices":[int(m.group(1)) for m in matches],"cloze_answer_words":[len(words(v)) for v in answers],"front_characters":len(_plain(text)),"extra_words":len(words(extra)),"answer_visible":any(v and re.search(rf"(?:^| ){re.escape(v)}(?: |$)",normalized(visible)) for v in map(normalized,answers)),"probable_language":"en" if sum(t in {"the","is","are","with","when","which","that","from","into","because"} for t in normalized(visible+" "+extra).split())>=3 else "pt-BR"}
def media_hashes(manifest_or_deck:dict[str,Any])->list[dict[str,str]]:
 return [{"key":str(i.get("key") or ""),"sha256":str(i.get("sha256") or "")} for i in (manifest_or_deck.get("media") or []) if isinstance(i,dict)]
def referenced_media_hashes(cards:list[dict[str,Any]],base:Path)->list[dict[str,str]]:
 out=[]
 for c in cards:
  raw=c.get("image_path")
  if not raw: continue
  path=Path(str(raw)); path=path if path.is_absolute() else (base/path).resolve(); out.append({"card_key":str(c.get("card_key") or ""),"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
 return out
