#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Renumera os blanks de cloze de cada card em sequencia c1..cN (atomicidade AnKing).
Fatos independentes que reusavam c1 passam a c1/c2/c3 -> um card por blank.
Reescreve os JSONs in place (backup .bak)."""
import json, sys, re, shutil

def renum(text):
    counter = [0]
    def repl(m):
        counter[0] += 1
        return "{{c%d::" % counter[0]
    return re.sub(r'\{\{c\d+::', repl, text)

for path in sys.argv[1:]:
    spec = json.load(open(path, encoding='utf-8'))
    changed = 0
    for c in spec['cards']:
        new = renum(c['text'])
        if new != c['text']:
            changed += 1
            c['text'] = new
    shutil.copy(path, path + '.bak')
    json.dump(spec, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(f"{path.split('/')[-1]}: {changed} cards renumerados")
