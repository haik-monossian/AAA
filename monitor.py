import psutil
import time
import platform
import socket
import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

# --- data ---

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
    
    # Ip adress
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
    # process
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            cpu = proc.cpu_percent(interval=0.1)
            mem = proc.memory_percent()
            processes.append({
                'name': proc.info['name'],
                'cpu_percent': round(cpu, 2),
                'memory_percent': round(mem, 2)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    # Top 3
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
        
        # Percentages
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

# --- Export json---

def main():
    """Fonction principale pour collecter les données et les exporter en JSON."""
    
    print("=" * 50)
    print("SURVEILLANCE SYSTÈME ET EXPORT JSON")
    print("=" * 50)
    
    directory = "." # Directory to analyse
    
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

    filename = "/var/www/html/system_report.json" # export filename
    
    # write data
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(system_data, f, indent=4) 
        
        print("\n" + "=" * 50)
        print(f"✅ Rapport système exporté vers : {filename}")
        print("=" * 50)
        
    except IOError as e:
        print(f"❌ Erreur lors de l'écriture du fichier JSON : {e}")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(30) # wait 30s