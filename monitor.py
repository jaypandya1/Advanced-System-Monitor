import psutil      # For getting system metrics (CPU, RAM, Disk)
import subprocess  # For running OS commands (Ping)
import platform    # To detect if we are on Windows or Linux
import datetime    # To add timestamps to our logs
import time        # To create delays if needed


class SystemMonitor:

 def __init__(self, thresholds):
        """
        The 'Constructor'. This runs automatically when we create a new Monitor.
        It saves the alert limits (thresholds) we want to use.
        """
        self.thresholds = thresholds
        self.os_type = platform.system()
        print(f"[{datetime.datetime.now()}] Monitor initialized on {self.os_type}...")

 def check_cpu(self):
        """Checks CPU usage."""
        # interval=1 blocks for 1 second to calculate accurate usage
        usage = psutil.cpu_percent(interval=1)
        status = "SAFE"

        if usage > self.thresholds['cpu']:
            status = "ALERT: High CPU Usage!"

        return usage, status

 def check_memory(self):
        """Checks RAM usage."""
        memory = psutil.virtual_memory()
        usage = memory.percent
        status = "SAFE"

        if usage > self.thresholds['ram']:
            status = "ALERT: Low Memory!"

        return usage, status

 def check_disk(self):
        """Checks Disk usage."""
        disk = psutil.disk_usage('/')
        usage = disk.percent
        status = "SAFE"

        if usage > self.thresholds['disk']:
            status = "ALERT: Disk Space Critical!"

        return usage, status

 def check_network(self, host="8.8.8.8"):
        """Pings Google DNS to check internet connectivity."""
        
        param = '-n' if self.os_type.lower() == 'windows' else '-c'
        command = ['ping', param, '1', host]

        try:
            # Run the ping command silently (capture output)
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if result.returncode == 0:
                return "UP", "Connection Stable"
            else:
                return "DOWN", "ALERT: Network Unreachable"
        except Exception as e:
            return "ERROR", str(e)

 def run_health_check(self):
        """The main method that orchestrates all checks."""
        print(f"\n--- SYSTEM HEALTH REPORT : {datetime.datetime.now()} ---")

        # 1. CPU
        cpu_val, cpu_msg = self.check_cpu()
        print(f"CPU Usage:    {cpu_val}%\t[{cpu_msg}]")

        # 2. RAM
        ram_val, ram_msg = self.check_memory()
        print(f"RAM Usage:    {ram_val}%\t[{ram_msg}]")

        # 3. DISK
        disk_val, disk_msg = self.check_disk()
        print(f"Disk Usage:   {disk_val}%\t[{disk_msg}]")

        # 4. NETWORK
        net_stat, net_msg = self.check_network()
        print(f"Network:      {net_stat}\t[{net_msg}]")
        print("-" * 50)

# --- EXECUTION STARTS HERE ---
if __name__ == "__main__":
    # Define our "Danger Zones"
    ALERT_LIMITS = {
        'cpu': 80,   # Alert if CPU is over 80%
        'ram': 80,   # Alert if RAM is over 80%
        'disk': 90   # Alert if Disk is over 90%
    }

    # Create the monitor object
    monitor = SystemMonitor(ALERT_LIMITS)

    # Run the check
    monitor.run_health_check()


