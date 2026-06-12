@echo off
python -m venv venv
call venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
echo Environment setup complete.
echo run run.sh app <operation> <arguments> to use the application.
