@echo off
title Campus Placement System
color 0A

echo ==================================================
echo   Campus Placement System - Setup and Launch
echo ==================================================
echo.

:: Check Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3.10+ from https://python.org
    pause
    exit /b 1
)

:: Create virtual environment if it doesn't exist
if not exist "venv\" (
    echo [1/5] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 ( echo ERROR: Failed to create venv & pause & exit /b 1 )
) else (
    echo [1/5] Virtual environment already exists, skipping...
)

:: Activate virtual environment
echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat

:: Install dependencies
echo [3/5] Installing dependencies...
pip install -r requirements.txt --quiet
if errorlevel 1 ( echo ERROR: pip install failed & pause & exit /b 1 )

:: Run migrations
echo [4/5] Setting up database...
python manage.py migrate --run-syncdb
if errorlevel 1 ( echo ERROR: Migration failed & pause & exit /b 1 )

:: Seed skills (safe to run multiple times)
python manage.py seed_skills

:: Create superuser only on first run
python manage.py shell -c "from placement.models import User; exit(0 if User.objects.exists() else 1)" >nul 2>&1
if errorlevel 1 (
    echo.
    echo [5/5] First run - create an admin account for /admin/
    echo       ^(press Ctrl+C to skip^)
    echo.
    python manage.py createsuperuser
) else (
    echo [5/5] Admin account already exists, skipping...
)

:: Launch server and open browser
echo.
echo ==================================================
echo   Starting server at http://127.0.0.1:8000/
echo   Press Ctrl+C to stop the server
echo ==================================================
echo.
start "" http://127.0.0.1:8000/
python manage.py runserver

pause
