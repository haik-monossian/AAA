Challenge Triple A - Dashboard de Monitoring

📋 Description
Projet de surveillance système en temps réel développé dans le cadre du Challenge Triple A - Phase 3 : Algorithmique.
Ce dashboard collecte et affiche des informations complètes sur votre système : processeur, mémoire, processus en cours, informations réseau et analyse de fichiers. L'objectif est de créer un outil de monitoring léger et efficace en Python.


🔧 Prérequis

Python 3.6+ installé sur votre système
pip (gestionnaire de paquets Python)
Système d'exploitation : Linux (Ubuntu), macOS ou Windows
Droits d'accès au système pour la lecture des processus


📦 Installation
1. Cloner ou télécharger le projet
git clone git@github.com:haik-monossian/AAA.git
2. Installer les dépendances
Sur Ubuntu/Linux :
bashsudo apt update
sudo apt install python3-pip
pip3 install psutil


🚀 Utilisation
Lancer le script de monitoring
Sur Linux/macOS :
bashpython3 monitor.py


✨ Fonctionnalités

🖥️ Informations Processeur

✅ Nombre de cœurs physiques
✅ Fréquence actuelle du CPU (MHz)
✅ Pourcentage d'utilisation CPU en temps réel

💾 Informations Mémoire

✅ RAM utilisée (en GB)
✅ RAM totale (en GB)
✅ Pourcentage d'utilisation de la RAM

🌐 Informations Système

✅ Nom de la machine (hostname)
✅ Système d'exploitation et version
✅ Heure de démarrage du système
✅ Temps écoulé depuis le démarrage (uptime)
✅ Nombre d'utilisateurs connectés
✅ Adresse IP principale

⚙️ Informations Processus

✅ Top 3 des processus les plus gourmands en CPU
✅ Top 3 des processus les plus gourmands en RAM
✅ Pourcentages détaillés pour chaque processus

📁 Analyse de Fichiers

✅ Scan récursif d'un dossier au choix
✅ Comptage par extension : .txt, .py, .pdf, .jpg
✅ Calcul du pourcentage de chaque type de fichier
✅ Total des fichiers analysés

==================================================
SURVEILLANCE SYSTÈME
==================================================

=== INFORMATIONS PROCESSEUR ===
Nombre de cœurs: 4
Fréquence actuelle: 2400.00 MHz
Utilisation CPU: 23.50%

=== INFORMATIONS MÉMOIRE ===
RAM utilisée: 8.45 GB
RAM totale: 16.00 GB
Utilisation RAM: 52.81%

=== INFORMATIONS SYSTÈME ===
Nom de la machine: ubuntu-vm
Système d'exploitation: Linux 5.15.0
Heure de démarrage: 2025-12-09 08:30:15
Uptime: 2 jours, 5 heures
Utilisateurs connectés: 1
Adresse IP principale: 192.168.1.45

=== INFORMATIONS PROCESSUS ===

Top 3 processus par utilisation CPU:
1. firefox - CPU: 15.30%
2. gnome-shell - CPU: 8.20%
3. python3 - CPU: 5.40%

Top 3 processus par utilisation RAM:
1. firefox - RAM: 12.45%
2. chrome - RAM: 8.30%
3. code - RAM: 6.20%

=== ANALYSE FICHIERS (~) ===

Nombre de fichiers par extension:
.txt: 245 fichiers (35.50%)
.py: 128 fichiers (18.55%)
.pdf: 89 fichiers (12.90%)
.jpg: 228 fichiers (33.05%)

Total de fichiers analysés: 690

==================================================
Analyse terminée!
==================================================

👤 Auteur
Roven Melloul
Haik Monossian
Daroueche Mari

🎓 Challenge Triple A 

📄 Licence
Ce projet est réalisé dans un cadre pédagogique (Challenge Triple A).




