@echo off
title Installation des Polices d'Ecriture
echo ==============================================================
echo Lancement de l'installateur de polices (PowerShell)...
echo ==============================================================
cd /d "%~dp0"
powershell -ExecutionPolicy Bypass -File install_fonts.ps1
echo.
echo Operation terminee.
pause
