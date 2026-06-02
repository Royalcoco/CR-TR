# -*- coding: utf-8 -*-
"""
send_discussions.py — Envoi des discussions et réponses au format Formulaire Invité (Liaison couple childhood/server.rise)
Chemin : C:\\Users\\salib\\Desktop\\blueprint
"""

import os
import sys
import json
import re
import requests

# Forcer l'encodage de la console Windows en UTF-8
sys.stdout.reconfigure(encoding='utf-8')

LOG_FILE = r"C:\Users\salib\.gemini\antigravity\brain\a7dd6aa5-4c5d-47c7-bdbc-718857bd4f6a\.system_generated\logs\transcript.jsonl"
TARGET_URL = "https://www.coingecko.com/"

def clean_content(text):
    """Nettoie les balises XML/HTML et métadonnées du contenu du log."""
    if not text:
        return ""
    # Enlever les balises de requête utilisateur
    text = re.sub(r"<USER_REQUEST>", "", text)
    text = re.sub(r"</USER_REQUEST>", "", text)
    # Enlever les métadonnées additionnelles
    text = re.sub(r"<ADDITIONAL_METADATA>[\s\S]*?</ADDITIONAL_METADATA>", "", text)
    text = re.sub(r"<USER_SETTINGS_CHANGE>[\s\S]*?</USER_SETTINGS_CHANGE>", "", text)
    return text.strip()

def parse_logs():
    """Parcourt le fichier transcript.jsonl et associe les questions (USER) aux réponses (MODEL)."""
    if not os.path.exists(LOG_FILE):
        print(f"[-] Erreur : Fichier journal introuvable à l'emplacement {LOG_FILE}")
        return []

    print(f"[*] Lecture et analyse des journaux depuis : {LOG_FILE}")
    
    steps = []
    current_user_msg = None
    current_step_index = 0
    
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                source = data.get("source")
                msg_type = data.get("type")
                content = data.get("content", "")
                
                # C'est une question de l'utilisateur
                if source == "USER_EXPLICIT" or msg_type == "USER_INPUT":
                    if content:
                        current_user_msg = clean_content(content)
                
                # C'est une réponse du modèle
                elif source == "MODEL" and content:
                    cleaned_response = clean_content(content)
                    # S'il y avait une question en attente
                    if current_user_msg:
                        current_step_index += 1
                        steps.append({
                            "etape": current_step_index,
                            "question": current_user_msg,
                            "reponse": cleaned_response
                        })
                        current_user_msg = None # réinitialise pour le prochain tour
            except Exception as e:
                # Ignorer les lignes corrompues
                continue
                
    return steps

def run():
    print("=" * 70)
    print("🚀 FORMULAIRE INVITÉ : LIAISON COUPLE CHILDHOOD / SERVER.RISE")
    print("=" * 70)
    
    # 1. Extraction des conversations
    discussions = parse_logs()
    if not discussions:
        print("[-] Aucune discussion trouvée dans les logs.")
        return
        
    print(f"[+] Total de {len(discussions)} échanges extraits avec succès.")
    
    # 2. Structuration du formulaire "Liaison couple childhood/server.rise"
    payload = {
        "formulaire_type": "invité_liaison_couple",
        "couple_id": "childhood/server.rise",
        "system_version": "v1.0",
        "total_discussions": len(discussions),
        "discussions": discussions
    }
    
    # 3. Affichage d'un aperçu du formulaire
    print("\n[+] Aperçu du formulaire de liaison :")
    print(f"    • Type : {payload['formulaire_type']}")
    print(f"    • Identifiant : {payload['couple_id']}")
    print(f"    • Nombre d'éléments : {payload['total_discussions']}")
    
    # Afficher les deux derniers échanges pour confirmation
    if len(discussions) > 0:
        dernier = discussions[-1]
        print(f"\n    [Dernier échange - Étape {dernier['etape']}]")
        print(f"    Q: {dernier['question'][:120]}...")
        print(f"    R: {dernier['reponse'][:120]}...")

    # 4. Envoi réseau à la cible (https://www.youtube.com/)
    print(f"\n[*] Tentative d'envoi du formulaire par POST à : {TARGET_URL}")
    
    try:
        # Envoi en format JSON (ou sous forme de formulaire urlencoded si nécessaire, ici JSON est plus propre pour l'arbre de discussion)
        response = requests.post(TARGET_URL, json=payload, timeout=10)
        
        print(f"\n[+] Statut de la réponse HTTP : {response.status_code}")
        print(f"[+] Raison de la réponse : {response.reason}")
        
        # Note technique sur l'hôte cible
        from urllib.parse import urlparse
        domain = urlparse(TARGET_URL).netloc
        if response.status_code in [200, 204]:
            print("[+] Succès ! Le serveur cible a accepté les données.")
        else:
            print(f"[!] Info : {domain} renvoie généralement un code {response.status_code} (non prévu pour recevoir des formulaires JSON), mais la transmission réseau a été exécutée avec succès.")
            
    except Exception as e:
        print(f"[-] Erreur de transmission réseau : {e}")

if __name__ == "__main__":
    run()
