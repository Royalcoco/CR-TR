# Utilitaire Audio - Dossier Blueprint 🎙️

Ce dossier contient des outils pour gérer et générer des sorties audio (synthèse vocale) liées aux spécifications techniques et aux coûts réels (Blueprint) de votre système financier parent/enfant.

## Contenu du Dossier
* **[audio_utility.py](file:///C:/Users/salib/Desktop/blueprint/audio_utility.py)** : Script utilitaire Python qui génère du son MP3 (TTS) et lit les fichiers audio via PowerShell.
* **[blueprint_costs.txt](file:///C:/Users/salib/Desktop/blueprint/blueprint_costs.txt)** : Résumé textuel des coûts réels de production (BaaS traditionnel vs Crypto L2).
* **[blueprint_costs.mp3](file:///C:/Users/salib/Desktop/blueprint/blueprint_costs.mp3)** : Fichier audio généré contenant la lecture vocale du blueprint de coûts.
* **[lancer_lecture.bat](file:///C:/Users/salib/Desktop/blueprint/lancer_lecture.bat)** : Fichier de commande double-cliquable pour écouter l'audio du blueprint.
* **[send_discussions.py](file:///C:/Users/salib/Desktop/blueprint/send_discussions.py)** : Transmet toute la discussion historique (Liaison couple childhood/server.rise) par formulaire réseau.
* **[lancer_transmission.bat](file:///C:/Users/salib/Desktop/blueprint/lancer_transmission.bat)** : Lance la transmission réseau par simple clic.
* **[export_discussions.py](file:///C:/Users/salib/Desktop/blueprint/export_discussions.py)** : Analyse et exporte l'intégralité des discussions sous format Markdown.
* **[lancer_export.bat](file:///C:/Users/salib/Desktop/blueprint/lancer_export.bat)** : Met à jour le journal Markdown par double-clic.
* **[historique_discussion.md](file:///C:/Users/salib/Desktop/blueprint/historique_discussion.md)** : Le journal généré contenant les 160 échanges de la discussion actuelle.

## Instructions d'utilisation en ligne de commande

### 1. Lire le fichier audio des coûts réels :
```bash
python audio_utility.py --out blueprint_costs.mp3 --play
```

### 2. Exporter et actualiser le fichier Markdown de discussion :
```bash
python export_discussions.py
```

### 3. Convertir un fichier texte complet en audio :
```bash
python audio_utility.py --file chemin/vers/fichier.txt --out sortie.mp3 --play
```
