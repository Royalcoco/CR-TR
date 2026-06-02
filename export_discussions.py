# -*- coding: utf-8 -*-
"""
export_discussions.py — Extrait toute la discussion historique et génère un document Markdown lisible.
Chemin : C:\\Users\\salib\\Desktop\\blueprint
"""

import os
import sys
import json
import re

# Encodage console UTF-8
sys.stdout.reconfigure(encoding='utf-8')

LOG_FILE = r"C:\Users\salib\.gemini\antigravity\brain\a7dd6aa5-4c5d-47c7-bdbc-718857bd4f6a\.system_generated\logs\transcript.jsonl"
OUTPUT_MD = r"C:\Users\salib\Desktop\blueprint\historique_discussion.md"

def clean_content(text):
    """Nettoie le texte des balises système et méta-données pour une lecture propre."""
    if not text:
        return ""
    # Retirer les balises de requêtes utilisateur
    text = re.sub(r"<USER_REQUEST>", "", text)
    text = re.sub(r"</USER_REQUEST>", "", text)
    # Retirer les settings change et métadonnées additionnelles
    text = re.sub(r"<ADDITIONAL_METADATA>[\s\S]*?</ADDITIONAL_METADATA>", "", text)
    text = re.sub(r"<USER_SETTINGS_CHANGE>[\s\S]*?</USER_SETTINGS_CHANGE>", "", text)
    # Remplacer les sauts de ligne multiples
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()

def run_export():
    if not os.path.exists(LOG_FILE):
        print(f"[-] Erreur : Impossible de localiser le journal : {LOG_FILE}")
        return
        
    print(f"[*] Lecture de l'historique depuis {LOG_FILE}...")
    
    markdown_content = []
    markdown_content.append("# 📖 Historique Complet des Discussions — Liaison childhood/server.rise\n")
    markdown_content.append("Ce document contient l'intégralité des échanges (questions utilisateur et réponses de l'agent IA) extraits du journal système.\n")
    markdown_content.append("---\n")
    
    current_user_msg = None
    step_count = 0
    
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                source = data.get("source")
                msg_type = data.get("type")
                content = data.get("content", "")
                
                if source == "USER_EXPLICIT" or msg_type == "USER_INPUT":
                    if content:
                        current_user_msg = clean_content(content)
                        
                elif source == "MODEL" and content:
                    cleaned_response = clean_content(content)
                    if current_user_msg:
                        step_count += 1
                        markdown_content.append(f"## 👤 Échange {step_count} — Question Utilisateur\n")
                        markdown_content.append(f"{current_user_msg}\n\n")
                        markdown_content.append(f"### 🤖 Échange {step_count} — Réponse de l'Assistant\n")
                        markdown_content.append(f"{cleaned_response}\n")
                        markdown_content.append("\n---\n")
                        current_user_msg = None
            except Exception as e:
                continue
                
    # Sauvegarde du fichier Markdown
    with open(OUTPUT_MD, "w", encoding="utf-8") as out_f:
        out_f.write("\n".join(markdown_content))
        
    print(f"[+] Succès ! {step_count} échanges intégrés dans le document : {OUTPUT_MD}")

if __name__ == "__main__":
    run_export()
