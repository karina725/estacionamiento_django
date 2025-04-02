#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
#pip install -r requierements.txt

python manager.py collectstatic --no-input
python manager.py migrate
