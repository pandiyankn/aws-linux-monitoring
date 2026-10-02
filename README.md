# AWS Linux Server Monitoring and Automated Alert System

A beginner-to-intermediate **Cloud/DevOps monitoring project** that monitors Linux server health using Python and `psutil`, records system metrics in log files, and is designed for deployment on **AWS EC2** with **CloudWatch and SNS alerts**.

The project combines **Python, Linux, AWS, DevOps, and networking concepts** into a practical server-monitoring solution.

---

## 🚀 Project Overview

In real-world cloud environments, servers need to be continuously monitored for resource usage and availability.

This project monitors:

* CPU usage
* Memory usage
* Disk usage
* Network traffic
* Server health status

When resource usage crosses configured thresholds, the application generates warning messages and records them in a log file.

The planned AWS deployment extends this monitoring system with:

* AWS EC2
* IAM
* Amazon CloudWatch
* Amazon SNS
* Linux server administration

---

## 🏗️ Architecture

```text
                    AWS Cloud
                       │
                       ▼
              ┌─────────────────┐
              │     AWS EC2     │
              │  Linux Server   │
              └────────┬────────┘
                       │
                       ▼
             ┌───────────────────┐
             │ Python Monitoring │
             │     Application   │
             └─────────┬─────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
      CPU           Memory          Disk
        │              │              │
        └──────────────┼──────────────┘
                       │
                       ▼
                Server Status
                       │
              ┌────────┴────────┐
              ▼                 ▼
        Local Logging       CloudWatch
                                │
                                ▼
                          CloudWatch Alarm
                                │
                                ▼
                             AWS SNS
                                │
                                ▼
                          Email Alert
```

---

## 🛠️ Technologies Used

| Technology        | Purpose                                        |
| ----------------- | ---------------------------------------------- |
| Python            | Monitoring application                         |
| psutil            | Collect system resource metrics                |
| Linux             | Server operating system                        |
| AWS EC2           | Cloud server                                   |
| AWS IAM           | Access control                                 |
| Amazon CloudWatch | Monitoring and alarms                          |
| Amazon SNS        | Email notifications                            |
| Git               | Version control                                |
| GitHub            | Source code management                         |
| Networking        | VPC, subnet, IP, routing and security concepts |

---

## 📂 Project Structure

```text
aws-linux-monitoring/
│
├── monitor.py
├── config.py
├── requirements.txt
├── .gitignore
├── README.md
└── monitoring.log
```

Generated/runtime files such as `monitoring.log`, `__pycache__`, and virtual environments are excluded from Git using `.gitignore`.

---

## ⚙️ Features

### 1. CPU Monitoring

The application checks the current CPU utilization.

Default threshold:

```text
80%
```

If CPU usage exceeds the threshold:

```text
WARNING - High CPU usage
```

---

### 2. Memory Monitoring

The application monitors RAM utilization.

Default threshold:

```text
80%
```

---

### 3. Disk Monitoring

The application checks disk utilization.

Default threshold:

```text
80%
```

---

### 4. Network Monitoring

The application collects:

* Bytes sent
* Bytes received

Example:

```text
Network Sent=47399603 bytes
Network Received=1648404136 bytes
```

---

### 5. Server Health Status

The application determines the overall server status.

```text
HEALTHY
```

or

```text
WARNING
```

---

### 6. Logging

Monitoring information is written to:

```text
monitoring.log
```

Example:

```text
CPU=9.3% | Memory=63.5% | Disk=95.4% |
Network Sent=47435581 bytes |
Network Received=1648417278 bytes |
Status=WARNING
```

---

## 🔧 Configuration

Monitoring thresholds are maintained separately in `config.py`.

```python
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

MONITOR_INTERVAL = 5
```

This allows thresholds and monitoring intervals to be changed without modifying the main monitoring program.

---

## 💻 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/pandiyankn/aws-linux-monitoring.git
```

Move into the project:

```bash
cd aws-linux-monitoring
```

---

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Start monitoring

```bash
python monitor.py
```

The application continuously monitors the system.

Stop it with:

```text
Ctrl + C
```

---

## 📊 Sample Output

```text
CPU=0.0% | Memory=63.5% | Disk=95.4% |
Network Sent=47399603 bytes |
Network Received=1648404136 bytes |
Status=WARNING
```

Another example:

```text
CPU=9.3% | Memory=63.5% | Disk=95.4% |
Network Sent=47435581 bytes |
Network Received=1648417278 bytes |
Status=WARNING
```

The `WARNING` status is generated because one or more configured resource thresholds have been exceeded.

---

# ☁️ AWS Deployment Plan

The application is designed to be deployed on an AWS Linux EC2 instance.

### Step 1 — Launch EC2

Create an EC2 instance using a Linux-based AMI.

Example:

```text
Amazon Linux
```

---

### Step 2 — Configure Networking

The EC2 instance will use:

* VPC
* Subnet
* Private/Public IP
* Route table
* Internet Gateway
* Security Group

These components provide the networking foundation required for the server.

---

### Step 3 — Configure IAM

Attach an IAM role to the EC2 instance so the server can interact with AWS monitoring services without storing AWS access keys inside the application.

---

### Step 4 — Install Python Dependencies

On the EC2 Linux server:

```bash
sudo dnf update -y
```

Install Python:

```bash
sudo dnf install python3 -y
```

Install the required package:

```bash
pip3 install psutil
```

---

### Step 5 — Deploy the Application

Clone the GitHub repository:

```bash
git clone https://github.com/pandiyankn/aws-linux-monitoring.git
```

Run:

```bash
cd aws-linux-monitoring
python3 monitor.py
```

---

# 📈 CloudWatch Integration

The AWS version of this project will integrate with **Amazon CloudWatch**.

CloudWatch will be used to monitor server metrics and create alarms based on configured thresholds.

Example:

```text
CPU > 80%
       ↓
CloudWatch Alarm
       ↓
SNS Notification
       ↓
Email Alert
```

---

# 📧 SNS Alerting

Amazon SNS will be used for notifications.

Example alert:

```text
Subject:
EC2 Server Monitoring Alert

Message:
CPU usage has exceeded the configured threshold.
```

This provides an automated alerting mechanism instead of requiring someone to continuously watch the server.

---

# 🔐 Security Considerations

The project follows basic cloud security practices:

* IAM roles instead of hard-coded AWS credentials
* Security Groups to control network access
* `.gitignore` for sensitive/local files
* No private keys committed to Git
* No AWS credentials stored in source code

The following are excluded from Git:

```text
*.pem
.env
venv/
__pycache__/
monitoring.log
```

---

# 🧠 Skills Demonstrated

This project demonstrates practical knowledge of:

### Python

* Functions
* Variables
* Conditional statements
* Loops
* Modules
* Exception/interrupt handling
* External packages
* Logging

### Linux

* Linux server administration
* Python execution
* Package installation
* File permissions
* Process management
* Server monitoring

### AWS

* EC2
* IAM
* CloudWatch
* SNS
* VPC
* Security Groups

### Networking / CCNA

* IP addressing
* Public and private IP concepts
* Subnets
* Routing
* Internet Gateway
* DNS
* Network connectivity
* Security Groups

### DevOps

* Git
* GitHub
* Linux
* Monitoring
* Logging
* Automation
* Cloud infrastructure

---

# 🔮 Future Enhancements

Possible improvements include:

* CloudWatch custom metrics
* SNS email alerts
* EC2 automatic recovery
* Systemd service for automatic application startup
* Docker containerization
* GitHub Actions CI/CD
* Terraform infrastructure automation
* Kubernetes deployment
* Grafana dashboards
* Prometheus monitoring
* Automated health checks
* Centralized logging

---

# 🎯 Project Goal

The goal of this project is to demonstrate how a Python-based monitoring application can be integrated with cloud infrastructure and DevOps practices to monitor Linux servers and generate automated alerts.

It is designed as a practical project for demonstrating **Cloud Computing, AWS, Linux, Python, Networking, and DevOps fundamentals**.

---

## 👨‍💻 Author

**Pandiyan KN**

GitHub:

https://github.com/pandiyankn
