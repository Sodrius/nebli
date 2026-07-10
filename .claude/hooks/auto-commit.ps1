# auto-commit.ps1
# Stop hook: roda quando o Claude termina o turno. Se houver mudancas
# no working tree, faz `git add -A && git commit -m "auto: ..."`.
# Silencioso quando nao ha mudancas.
#
# Autor inline (Davi Sousa <dpbdes@gmail.com>) para nao tocar em
# config global do git. Canonico 2026-05-22 (P45).

$ErrorActionPreference = 'SilentlyContinue'
Set-Location -LiteralPath 'C:\AI use\nebli'

# Se nao for um repositorio git, sai silencioso.
$insideRepo = git rev-parse --is-inside-work-tree 2>$null
if ($insideRepo -ne 'true') { exit 0 }

# Detecta mudancas (staged ou nao-staged ou untracked).
$changes = git status --porcelain 2>$null
if (-not $changes) { exit 0 }

# Lista os primeiros 3 arquivos modificados para a mensagem.
$lines = @($changes -split "`n" | Where-Object { $_.Trim() -ne '' })
$nomes = @()
foreach ($l in $lines | Select-Object -First 3) {
    # status sao 2 chars + espaco + path. Pega so o path.
    $path = $l.Substring(3).Trim().Trim('"')
    $nomes += [System.IO.Path]::GetFileName($path)
}
$extra = if ($lines.Count -gt 3) { " (+$($lines.Count - 3))" } else { '' }
$ts = Get-Date -Format 'yyyy-MM-dd HH:mm'
$msg = "auto: $ts -- $($nomes -join ', ')$extra"

git add -A 2>&1 | Out-Null
git -c user.name='Davi Sousa' -c user.email='dpbdes@gmail.com' commit -m $msg 2>&1 | Out-Null

# Se quiser ver no terminal que o hook rodou, descomentar:
# Write-Host "[auto-commit] $msg"

exit 0
