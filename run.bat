@echo off
REM Data Generator Batch File for Windows

echo ==========================================
echo Data Generator for Weight ^& Strength
echo ==========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found!
    echo Please install Python 3.7 or higher
    pause
    exit /b 1
)

REM Run the data generator
python data_generator.py
pause
