@echo off
call venv\Scripts\activate
python caching-proxy.py %*
