@echo off
echo ========================================
echo    Bytie Chatbot Backend Server
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo Python found!
echo.

REM Check if Flask is installed
python -c "import flask" 2>nul
if errorlevel 1 (
    echo Flask not found. Installing dependencies...
    pip install -r requirements.txt
    echo.
)

echo Starting Bytie chatbot server...
echo.
echo Server will run on http://localhost:5000
echo Keep this window open while using the chatbot
echo Press Ctrl+C to stop the server
echo.
echo ========================================
echo.

python chatbot_backend.py

pause
