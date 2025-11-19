# 🐍 Advanced System Monitor (v1.0)

A modular, Object-Oriented Python utility designed for proactive system monitoring and triage. This tool simulates a real DevOps health check by measuring critical host resource utilization (CPU, RAM, Disk) and external network connectivity against defined thresholds.

**🎯 Built By:** [Jay Pandya/jaypandya1]

## 💡 Why This Project? 

This project was developed to transition my troubleshooting experience from Service Desk into a core Cloud Support / Junior DevOps skillset.

It directly demonstrates:

1.  **Automation:** Replacing manual terminal checks (`top`, `df -h`, `ping`) with a single, repeatable Python script.
2.  **Troubleshooting Logic:** Utilizing code (`if/else`) to immediately identify root causes (e.g., distinguishing between a network failure and a memory bottleneck).
3.  **Clean Code:** Employing Object-Oriented Programming (OOP) to build reusable, maintainable code structures.

## 🛠️ Tech Stack & Core Modules

| Component | Technology | Purpose in Project |
| :--- | :--- | :--- |
| **Language** | Python 3 | Core scripting logic (using your Codecademy OOP skills). |
| **System Metrics** | `psutil` | Standard cross-platform library for retrieving CPU, RAM, and Disk utilization. |
| **Command Execution** | `subprocess` | Python's recommended library for running external OS commands (like `ping`). |
| **Code Structure** | Python `class` | Used to encapsulate methods, ensuring high modularity. |

## 🚀 Getting Started

Follow these steps to clone the repository and run the health check on your local machine (Linux/macOS/WSL).

### Prerequisites

You must have Python 3.x and `pip` installed.

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/advanced-system-monitor.git](https://github.com/YOUR_USERNAME/advanced-system-monitor.git)
    cd advanced-system-monitor
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

Run the main script directly from your terminal:

```bash
python monitor.py


### Sample Output

--- SYSTEM HEALTH REPORT : 2025-11-19 15:30:00 ---
CPU Usage:    12.5%     [SAFE]
RAM Usage:    45.2%     [SAFE]
Disk Usage:   22.0%     [SAFE]
Network:      UP        [Connection Stable]
--------------------------------------------------

