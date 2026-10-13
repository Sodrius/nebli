#!/bin/zsh
cd /Users/davisousa/NEBLI
for t in 2026-uc03-bioquimica-25-integracao-metabolica-i 2026-uc03-microbiologia-27-fisiologia-bacteriana 2026-uc03-microbiologia-28-pratica-1 2026-uc03-biologia-molecular-29-operon-procariotos; do
  python3 -m nebli.explicacoes gerar "tag:NEBLI::$t"
done
echo FIM
