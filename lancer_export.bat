@echo off
title Export de l'Historique de Discussion
echo ==============================================================
echo Generation du fichier historique_discussion.md...
echo ==============================================================
cd /d "%~dp0"
"C:\Users\salib\.gemini\antigravity\scratch\crypto_audio_cli\.venv\Scripts\python.exe" export_discussions.py
echo.
echo Export termine.
pause
