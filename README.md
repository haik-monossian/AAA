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

👤 Auteur
Roven Melloul
Haik Monossian
Daroueche Mari

🎓 Challenge Triple A 

📄 Licence
Ce projet est réalisé dans un cadre pédagogique (Challenge Triple A).




