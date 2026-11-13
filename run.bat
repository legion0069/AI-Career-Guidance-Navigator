@echo off
echo ========================================================
echo        Starting AI Career Guidance Navigator
echo ========================================================
echo.
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in your PATH.
    pause
    exit /b
)

echo Starting FastAPI server at http://127.0.0.1:8000 ...
python app.py
pause

