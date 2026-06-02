# -*- coding: utf-8 -*-
"""
audio_utility.py — Utilitaire audio de génération et de lecture de synthèse vocale (TTS)
Chemin d'utilisation : C:\\Users\\salib\\Desktop\\blueprint
"""

import os
import sys
import argparse
import subprocess
import threading

# Reconfigurer la sortie pour gérer correctement les encodages UTF-8 dans la console Windows
sys.stdout.reconfigure(encoding='utf-8')

# Détermination automatique de l'interpréteur Python avec l'environnement virtuel pour gTTS
VENV_PYTHON = r"C:\Users\salib\.gemini\antigravity\scratch\crypto_audio_cli\.venv\Scripts\python.exe"

def check_gtts():
    """Vérifie si gTTS est disponible ou tente d'importer gtts."""
    try:
        from gtts import gTTS
        return True
    except ImportError:
        return False

def play_audio_file(file_path):
    """Joue un fichier MP3 de manière asynchrone sous Windows via PowerShell (WMPlayer.OCX)."""
    abs_path = os.path.abspath(file_path)
    if not os.path.exists(abs_path):
        print(f"[-] Erreur : Le fichier {abs_path} n'existe pas.")
        return False
        
    print(f"[>] Lecture de l'audio : {os.path.basename(abs_path)}...")
    
    # Commande PowerShell pour démarrer la lecture via l'objet COM Windows Media Player
    ps_cmd = (
        f"$player = New-Object -ComObject WMPlayer.OCX; "
        f"$player.URL = '{abs_path}'; "
        f"$player.controls.play(); "
        f"while ($player.playState -ne 1) {{ Start-Sleep -Milliseconds 100 }}"
    )
    cmd = ["powershell", "-Command", ps_cmd]
    
    # Exécuter dans un thread séparé pour ne pas bloquer l'appelant
    def _run():
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[+] Fin de la lecture de {os.path.basename(abs_path)}")
        
    thread = threading.Thread(target=_run)
    thread.start()
    return True

def generate_tts(text, output_path, lang="fr"):
    """Génère un fichier MP3 à partir du texte avec gTTS."""
    print(f"[*] Génération de l'audio (Langue: {lang})...")
    try:
        from gtts import gTTS
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(output_path)
        print(f"[+] Fichier audio généré avec succès dans : {output_path}")
        return True
    except Exception as e:
        print(f"[-] Erreur lors de la génération gTTS : {e}")
        print("[!] Tentative d'utilisation de l'environnement virtuel...")
        # Fallback via un sous-processus utilisant le venv
        inline_code = (
            f"from gtts import gTTS; "
            f"tts = gTTS(text={repr(text)}, lang={repr(lang)}, slow=False); "
            f"tts.save({repr(output_path)})"
        )
        try:
            res = subprocess.run(
                [VENV_PYTHON, "-c", inline_code],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            if res.returncode == 0:
                print(f"[+] Fichier audio généré via venv dans : {output_path}")
                return True
            else:
                print(f"[-] Échec via venv : {res.stderr}")
                return False
        except Exception as ex:
            print(f"[-] Erreur fatale : {ex}")
            return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Utilitaire Audio pour le dossier Blueprint")
    parser.add_argument("--text", type=str, help="Texte à convertir en audio")
    parser.add_argument("--file", type=str, help="Chemin d'un fichier texte à convertir en audio")
    parser.add_argument("--out", type=str, default="blueprint_output.mp3", help="Nom du fichier audio de sortie (MP3)")
    parser.add_argument("--play", action="store_true", help="Lire le fichier audio généré après traitement")
    parser.add_argument("--lang", type=str, default="fr", help="Code langue (fr, en, es...)")
    
    args = parser.parse_args()
    
    # Détermination du texte à traiter
    target_text = ""
    if args.text:
        target_text = args.text
    elif args.file:
        if os.path.exists(args.file):
            with open(args.file, "r", encoding="utf-8") as f:
                target_text = f.read()
        else:
            print(f"[-] Le fichier texte spécifié n'existe pas : {args.file}")
            sys.exit(1)
            
    if target_text:
        # Résolution du chemin de sortie dans le répertoire courant de blueprint
        out_path = os.path.abspath(args.out)
        success = generate_tts(target_text, out_path, lang=args.lang)
        if success and args.play:
            play_audio_file(out_path)
            # Attendre un peu que le thread de lecture commence
            import time
            time.sleep(2)
    else:
        # Si aucun texte n'est fourni, mode de lecture simple si un fichier est fourni avec --play
        if args.play and args.out and os.path.exists(args.out):
            play_audio_file(args.out)
        else:
            parser.print_help()
