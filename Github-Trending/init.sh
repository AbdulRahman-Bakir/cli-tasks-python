#!/bin/bash
python3 -m venv venv
source venv/bin/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
echo "Environment setup complete."
echo "Run './run.sh --duration week --limit 10' to use the application."