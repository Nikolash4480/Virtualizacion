import psutil

def get_hardware_info():
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
        "disk_used_percent": disk.percent
    }

# Ejecutar y mostrar
info = get_hardware_info()
print(info)