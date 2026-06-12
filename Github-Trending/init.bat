@echo off
python -m venv venv
call venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
echo Environment setup complete.
echo run run.bat --duration week --limit 10 to use the application.
