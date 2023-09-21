#!/bin/bash

script="main.py"

if [ ! -d "venv" ]; then
  echo "venv does not exist, creating"
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
else
  source venv/bin/activate
fi

python "$script"
deactivate
