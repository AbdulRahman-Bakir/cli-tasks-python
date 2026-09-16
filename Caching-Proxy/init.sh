#!/bin/bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
echo "Environment setup complete."
echo "Run './run.sh --port 3000 --origin http://dummyjson.com' to use the application."
