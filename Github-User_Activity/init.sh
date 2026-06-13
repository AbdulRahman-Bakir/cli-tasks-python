#!/bin/bash
python3 -m venv venv
source venv/bin/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
echo "Initialization complete."
echo "Please create a .env file with your GitHub token based on .env.example"
echo "Then run './run.sh <github_username> [event_type]' to use the application."