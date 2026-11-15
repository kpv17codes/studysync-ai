
$ErrorActionPreference = "Stop"

Set-Location "$PSScriptRoot/backend"

python -m pytest tests -v
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python -m ruff check .
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python -m mypy --explicit-package-bases app
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "All backend checks passed!"
