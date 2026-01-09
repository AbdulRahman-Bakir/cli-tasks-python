@echo off
python -m venv venv
call venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
echo ----------Environment setup complete.--------
echo ----------Please create a .env file with your GitHub token based on .env.example.--------
echo ----------Then run run.bat "<github_username> [event_type]" to use the application.--------
