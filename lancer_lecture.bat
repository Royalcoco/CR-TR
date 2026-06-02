@echo off
title Lecture du Blueprint Audio
echo ==============================================
echo Lancement de la lecture audio du Blueprint...
echo ==============================================
cd /d "%~dp0"
"C:\Users\salib\.gemini\antigravity\scratch\crypto_audio_cli\.venv\Scripts\python.exe" audio_utility.py --out blueprint_costs.mp3 --play
echo Lecture lancee en arriere-plan.
pause
