@echo off
REM Start the Flask server
start cmd /k "python server.py"

REM Wait for the server to start (adjust time if necessary)
timeout /t 5 /nobreak >nul

REM Open the default web browser to the local Flask server
start "" "http://127.0.0.1:5000/"
