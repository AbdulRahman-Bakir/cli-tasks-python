@echo off
python -m venv venv
call venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
echo Environment setup complete.
echo run run.bat --type popular to use the application.
