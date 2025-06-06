import psutil
import json
from datetime import datetime

def get_hardware_info():
  """
  Devuelve el uso de CPU, cantidad de núcleos,
  memoria, y uso de disco
  """
  cpu_percent = psutil.cpu_percent(interval=1)
  cpu_count = psutil.cpu_count(logical=True)
  virtual_mem = psutil.virtual_memory()
  disk = psutil.disk_usage('/')
  return {
      "cpu_percent": cpu_percent,
      "cpu_count": cpu_count,
      "memory_total_mb": round(virtual_mem.total / (1024 ** 2), 2),
      "memory_available_mb": round(virtual_mem.available / (1024 ** 2), 2),
      "memory_used_percent": virtual_mem.percent,
      "disk_total_gb": round(disk.total / (1024 ** 3), 2),
      "disk_used_gb": round(disk.used / (1024 ** 3), 2),
      "disk_free_gb": round(disk.free / (1024 ** 3), 2),
      "disk_used_percent": disk.percent,
      "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  }

def main():
  """Ejecuta y muestra la información del hardware"""
  try:
    info = get_hardware_info()
    print("=== INFORMACIÓN DEL SISTEMA ===")
    print(f"Fecha y hora: {info['timestamp']}")
    print(f"CPU: {info['cpu_percent']}% ({info['cpu_count']} núcleos)")
    print(f"Memoria: {info['memory_used_percent']}% ({info['memory_available_mb']} MB disponibles de {info['memory_total_mb']} MB)")
    print(f"Disco: {info['disk_used_percent']}% ({info['disk_free_gb']} GB libres de {info['disk_total_gb']} GB)")
    
    # Opcional: guardar en JSON
    with open('hardware_log.json', 'w') as f:
        json.dump(info, f, indent=2)
    print("\nDatos guardados en hardware_log.json")
    
  except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
    main()