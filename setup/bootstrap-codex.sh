#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [ ! -f ".env" ]; then
  cp ".env.example" ".env"
  echo "Created .env from .env.example"
else
  echo ".env already exists; leaving it unchanged"
fi

python -m pip install -e ".[dev]"

echo "Bootstrap complete. Run: uvicorn miles_app.main:app --reload"
