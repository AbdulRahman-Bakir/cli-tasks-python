@echo off
python -m venv venv
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
echo Environment setup complete.
echo run run.bat --port 3000 --origin http://dummyjson.com to use the application.
