#!/bin/bash

pip install -r requirements.txt

python -m venv .venv
source .venv/bin/activate

export PYTHONPATH="$PWD"
