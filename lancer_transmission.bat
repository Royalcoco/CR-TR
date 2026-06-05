@echo off
title Transmission des Discussions - Liaison childhood/server.rise
echo ==============================================================
echo Lancement de la transmission des discussions vers YouTube...
echo ==============================================================
cd /d "%~dp0"
"C:\Users\salib\.gemini\antigravity\scratch\crypto_audio_cli\.venv\Scripts\python.exe" send_discussions.py
echo.
echo Transmission terminee.
pause
