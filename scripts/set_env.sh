#!/bin/bash

python3 -m venv .venv
echo 'pip install -r requirements.txt' >> .venv/bin/activate
source .venv/bin/activate
export PYTHONPATH="$PWD"
