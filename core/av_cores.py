from libs.imports import psutil, os

def getNextAvailableCore():
    total_cores = psutil.cpu_count(logical=False)
    current_process = psutil.Process(os.getpid())
    used_cores = []

    for proc in psutil.process_iter(['cpu_affinity']):
        try:
            affinity = proc.info['cpu_affinity']
            if affinity:
                used_cores.extend(affinity)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    used_cores = set(used_cores)

    for core in range(total_cores):
        if core not in used_cores:
            return core

    return 0