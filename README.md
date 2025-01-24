# Process Monitor

A simple Python script to monitor system processes in real-time using `psutil` and display them in a table with `PrettyTable`.

## Features
- Displays process details: PID, Name, CPU Usage (%), Memory Usage (MB), Status, and Starting Time.
- Shows total CPU and memory usage.
- Refreshes every second with real-time updates.

## Environment
This script is designed to run on **Linux** or **MacOS** systems.

## Installation
Clone the repository:
   ```bash
   git clone https://github.com/SMSehab//Process_Monitor.git
   cd process-monitor
```
   
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
+------------+---------------+----------------+------------------+---------+------------+
| Process ID | Process Name  | CPU Usage (%)  | Memory Usage (MB)| Status  | Start Time |
+------------+---------------+----------------+------------------+---------+------------+
|   12345    | python3       |     0.75%      |     25.36 MB     | running |  10:34:12  |
|   67890    | chrome        |     2.45%      |    150.20 MB     | running |  10:31:05  |
|   ...      | ...           |      ...       |       ...        |   ...   |    ...     |
+------------+---------------+----------------+------------------+---------+------------+

Total CPU Usage: 3.20%
Total Memory Usage: 1.20 GB

Press Ctrl+C to exit...

