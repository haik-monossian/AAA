# import psutil
# import platform
# import socket
# import os
# from datetime import datetime
# from pathlib import Path

# def get_cpu_info():
#     """Récupère les informations sur le processeur"""
#     print("\n=== INFORMATIONS PROCESSEUR ===")
#     print(f"Nombre de cœurs: {psutil.cpu_count(logical=False)}")
#     print(f"Fréquence actuelle: {psutil.cpu_freq().current:.2f} MHz")
#     print(f"Utilisation CPU: {psutil.cpu_percent(interval=1):.2f}%")

# def get_memory_info():
#     """Récupère les informations sur la mémoire"""
#     print("\n=== INFORMATIONS MÉMOIRE ===")
#     mem = psutil.virtual_memory()
#     print(f"RAM utilisée: {mem.used / (1024**3):.2f} GB")
#     print(f"RAM totale: {mem.total / (1024**3):.2f} GB")
#     print(f"Utilisation RAM: {mem.percent:.2f}%")

# def get_system_info():
#     """Récupère les informations système générales"""
#     print("\n=== INFORMATIONS SYSTÈME ===")
#     print(f"Nom de la machine: {socket.gethostname()}")
#     print(f"Système d'exploitation: {platform.system()} {platform.release()}")
    
#     boot_time = datetime.fromtimestamp(psutil.boot_time())
#     print(f"Heure de démarrage: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
#     uptime = datetime.now() - boot_time
#     print(f"Uptime: {uptime.days} jours, {uptime.seconds//3600} heures")
    
#     print(f"Utilisateurs connectés: {len(psutil.users())}")
    
#     # Récupère l'adresse IP principale
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(("8.8.8.8", 80))
#         ip = s.getsockname()[0]
#         s.close()
#         print(f"Adresse IP principale: {ip}")
#     except:
#         print("Adresse IP principale: Non disponible")

# def get_process_info():
#     """Récupère les informations sur les processus"""
#     print("\n=== INFORMATIONS PROCESSUS ===")
    
#     processes = []
#     for proc in psutil.process_iter(['pid', 'name']):
#         try:
#             # Mesure le CPU avec un intervalle court
#             cpu = proc.cpu_percent(interval=0.1)
#             mem = proc.memory_percent()
#             processes.append({
#                 'name': proc.info['name'],
#                 'cpu_percent': cpu,
#                 'memory_percent': mem
#             })
#         except (psutil.NoSuchProcess, psutil.AccessDenied):
#             pass
    
#     # Tri par CPU
#     processes_cpu = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)
#     print("\nTop 3 processus par utilisation CPU:")
#     for i, proc in enumerate(processes_cpu[:3], 1):
#         print(f"{i}. {proc['name']} - CPU: {proc['cpu_percent']:.2f}%")
    
#     # Tri par RAM
#     processes_mem = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)
#     print("\nTop 3 processus par utilisation RAM:")
#     for i, proc in enumerate(processes_mem[:3], 1):
#         print(f"{i}. {proc['name']} - RAM: {proc['memory_percent']:.2f}%")

# def analyze_files(directory):
#     """Analyse les fichiers dans un dossier"""
#     print(f"\n=== ANALYSE FICHIERS ({directory}) ===")
    
#     extensions = {'.txt': 0, '.py': 0, '.pdf': 0, '.jpg': 0}
    
#     try:
#         path = Path(directory).expanduser()
        
#         for file in path.rglob('*'):
#             if file.is_file():
#                 ext = file.suffix.lower()
#                 if ext in extensions:
#                     extensions[ext] += 1
        
#         total = sum(extensions.values())
        
#         print(f"\nNombre de fichiers par extension:")
#         for ext, count in extensions.items():
#             percentage = (count / total * 100) if total > 0 else 0
#             print(f"{ext}: {count} fichiers ({percentage:.2f}%)")
        
#         print(f"\nTotal de fichiers analysés: {total}")
        
#     except Exception as e:
#         print(f"Erreur lors de l'analyse: {e}")

# def main():
#     """Fonction principale"""
#     print("=" * 50)
#     print("SURVEILLANCE SYSTÈME")
#     print("=" * 50)
    
#     get_cpu_info()
#     get_memory_info()
#     get_system_info()
#     get_process_info()
    
#     # Choisissez le dossier à analyser
#     directory = ""  # Modifiez selon vos besoins: "/Documents", "~/Desktop", etc.
#     analyze_files(directory)
    
#     print("\n" + "=" * 50)
#     print("Analyse terminée!")
#     print("=" * 50)

# if __name__ == "__main__":
#     main()

import psutil
import platform
import socket
import os
import json # NOUVEAU: Importation du module json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any # Optionnel, pour la lisibilité

# --- Fonctions pour collecter les données ---

def get_cpu_info() -> Dict[str, Any]:
    """Récupère et retourne les informations sur le processeur"""
    freq = psutil.cpu_freq()
    return {
        "cores": psutil.cpu_count(logical=False),
        "current_frequency_mhz": round(freq.current, 2) if freq else None,
        "cpu_usage_percent": round(psutil.cpu_percent(interval=1), 2)
    }

def get_memory_info() -> Dict[str, Any]:
    """Récupère et retourne les informations sur la mémoire"""
    mem = psutil.virtual_memory()
    return {
        "ram_used_gb": round(mem.used / (1024**3), 2),
        "ram_total_gb": round(mem.total / (1024**3), 2),
        "ram_usage_percent": round(mem.percent, 2)
    }

def get_system_info() -> Dict[str, Any]:
    """Récupère et retourne les informations système générales"""
    
    boot_time_ts = psutil.boot_time()
    boot_time = datetime.fromtimestamp(boot_time_ts)
    uptime = datetime.now() - boot_time
    
    # Récupère l'adresse IP principale
    ip = "Non disponible"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except Exception:
        pass
        
    return {
        "machine_name": socket.gethostname(),
        "os_system": platform.system(),
        "os_release": platform.release(),
        "boot_time": boot_time.strftime('%Y-%m-%d %H:%M:%S'),
        "uptime_days": uptime.days,
        "uptime_hours": uptime.seconds // 3600,
        "logged_users": len(psutil.users()),
        "primary_ip_address": ip
    }

def get_process_info() -> Dict[str, Any]:
    """Récupère et retourne les informations sur les processus"""
    processes = []
    # Collecter les données de tous les processus
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Mesure le CPU avec un intervalle court
            cpu = proc.cpu_percent(interval=0.1)
            mem = proc.memory_percent()
            processes.append({
                'name': proc.info['name'],
                'cpu_percent': round(cpu, 2),
                'memory_percent': round(mem, 2)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    # Tri et sélection des Top 3
    processes_cpu = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)
    processes_mem = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)
    
    return {
        "top_3_cpu": processes_cpu[:3],
        "top_3_ram": processes_mem[:3],
        "total_processes_analyzed": len(processes)
    }

def analyze_files(directory: str) -> Dict[str, Any]:
    """Analyse les fichiers dans un dossier et retourne les statistiques"""
    extensions = {'.txt': 0, '.py': 0, '.pdf': 0, '.jpg': 0}
    total = 0
    
    try:
        path = Path(directory).expanduser()
        
        for file in path.rglob('*'):
            if file.is_file():
                ext = file.suffix.lower()
                total += 1
                if ext in extensions:
                    extensions[ext] += 1
        
        # Calculer les pourcentages
        stats = {}
        for ext, count in extensions.items():
            percentage = (count / total * 100) if total > 0 else 0
            stats[ext] = {
                "count": count,
                "percentage": round(percentage, 2)
            }
        
        return {
            "directory_analyzed": directory,
            "total_files_found": total,
            "file_counts_by_extension": stats
        }
    except Exception as e:
        return {"error": f"Analyse du fichier: {e}"}

# --- Fonction principale et Export JSON ---

def main():
    """Fonction principale pour collecter les données et les exporter en JSON."""
    
    print("=" * 50)
    print("SURVEILLANCE SYSTÈME ET EXPORT JSON")
    print("=" * 50)
    
    # Choisissez le dossier à analyser (Exemple: le répertoire courant)
    directory = "." # Modifiez selon vos besoins: "/home/user/Documents", etc.
    
    # 1. Collecter toutes les données
    print("Collecte des informations en cours...")
    
    system_data = {
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "cpu_info": get_cpu_info(),
        "memory_info": get_memory_info(),
        "system_info": get_system_info(),
        "process_info": get_process_info(),
        "file_analysis": analyze_files(directory)
    }
    
    print("Collecte terminée. Tentative d'export JSON.")

    # 2. Définir le nom du fichier de sortie
    filename = "system_report_" + datetime.now().strftime('%Y%m%d_%H%M%S') + ".json"
    
    # 3. Écrire les données dans le fichier JSON
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # json.dump est la commande clé pour écrire le dictionnaire Python dans le fichier
            # indent=4 rend le fichier JSON lisible
            json.dump(system_data, f, indent=4) 
        
        print("\n" + "=" * 50)
        print(f"✅ Rapport système exporté vers : {filename}")
        print("=" * 50)
        
    except IOError as e:
        print(f"❌ Erreur lors de l'écriture du fichier JSON : {e}")

if __name__ == "__main__":
    main()