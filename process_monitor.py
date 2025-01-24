from prettytable import PrettyTable
from datetime import datetime
import psutil
import time


def fetch_processes():
   
    processes = []
    total_cpu = 0.0
    total_memory = 0.0
    num_cores = psutil.cpu_count(logical=True)

    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'status', 'create_time']):
        try:
            # Extracting process details
            pid = process.info['pid']
            name = process.info['name'] or "Unknown"
            cpu = process.info['cpu_percent'] / num_cores  
            memory = process.info['memory_info'].rss / (1024 * 1024)  
            status = process.info['status']
            created = datetime.fromtimestamp(process.info['create_time']).strftime("%H:%M:%S")

            # Adding to totals
            total_cpu += cpu
            total_memory += memory / 1024  # Converting to GB


            processes.append([pid, name, f"{cpu:.2f}%", f"{memory:.2f} MB", status, created])
        
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Skip inaccessible processes
            continue

    # Sort by Status, Running time first
    processes.sort(key=lambda x: (x[4] != "running", x[4]))
    return processes, total_cpu, total_memory


def display_processes():

    while True:
        processes, total_cpu, total_memory = fetch_processes()

        table = PrettyTable()
        table.field_names = ["Process ID", "Process Name", "CPU Usage (%)", "Memory Usage (MB)", "Status", "Starting Time"]
        table.add_rows(processes)

        
        # Clear console
        print("\033c", end="")  
        print(table)
        
        print(f"Total CPU Usage: {total_cpu:.2f}%")
        print(f"Total Memory Usage: {total_memory:.2f} GB")
        print("\nPress Ctrl+C to exit...")

        time.sleep(1)


if __name__ == "__main__":
    display_processes()

