# Process Monitor

A simple Python script to monitor system processes in real-time using `psutil` and display them in a table with `PrettyTable`.

## Features
- Displays process details: PID, Name, CPU Usage (%), Memory Usage (MB), Status, and Starting Time.
- Shows total CPU and memory usage.
- Refreshes every second with real-time updates.

## Requirements
- Python 3.6+
- Install dependencies:
  ```bash
  pip install psutil prettytable
  
## Run the script
  ```bash
    python process_monitor.py

```
## Example Output
```bash
+------------+---------------+----------------+------------------+---------+---------------------+
| Process ID | Process Name  | CPU Usage (%)  | Memory Usage (MB)| Status  |    Active Time      |
+------------+---------------+----------------+------------------+---------+---------------------+
|   12345    | python3       |     0.75%      |     25.36 MB     | running | 2025-01-25 10:34:12 |
+------------+---------------+----------------+------------------+---------+---------------------+

Total CPU Usage: 3.20%
Total Memory Usage: 1.20 GB
