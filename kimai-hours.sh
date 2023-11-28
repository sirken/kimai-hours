#!/bin/bash

script="main.py"

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "$SCRIPT_DIR"

# only run Mon (1) to Fri (5)
if [ $(date +%u) -le 5 ]; then
  if [ ! -d "venv" ]; then
    echo "venv does not exist, creating"
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
  else
    source venv/bin/activate
  fi

  python "$script"
  deactivate
else
  echo ⚠
fi
