@echo off
title Demon de Flux Bancaire Continu v1.0
echo ==============================================================
echo Demarrage de la reception continue de flux bancaires...
echo ==============================================================
cd /d "%~dp0"
"C:\Users\salib\.gemini\antigravity\scratch\crypto_audio_cli\.venv\Scripts\python.exe" flux_bancaire.py
pause
