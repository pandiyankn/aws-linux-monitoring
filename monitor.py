import psutil
import time
import logging
from datetime import datetime

from config import (
    CPU_THRESHOLD,
    MEMORY_THRESHOLD,
    DISK_THRESHOLD,
    MONITOR_INTERVAL
)


logging.basicConfig(
    filename="monitoring.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_server_status():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    network = psutil.net_io_counters()
    bytes_sent = network.bytes_sent
    bytes_received = network.bytes_recv

    warnings = []

    if cpu > CPU_THRESHOLD:
        warnings.append("High CPU usage")

    if memory > MEMORY_THRESHOLD:
        warnings.append("High Memory usage")

    if disk > DISK_THRESHOLD:
        warnings.append("High Disk usage")

    if warnings:
        status = "WARNING"
    else:
        status = "HEALTHY"

    return (
        cpu,
        memory,
        disk,
        bytes_sent,
        bytes_received,
        status,
        warnings
    )


while True:

    (
        cpu,
        memory,
        disk,
        bytes_sent,
        bytes_received,
        status,
        warnings
    ) = get_server_status()

    message = (
        f"CPU={cpu}% | "
        f"Memory={memory}% | "
        f"Disk={disk}% | "
        f"Network Sent={bytes_sent} bytes | "
        f"Network Received={bytes_received} bytes | "
        f"Status={status}"
    )

    print(message)

    logging.info(message)

    for warning in warnings:
        logging.warning(warning)

    time.sleep(MONITOR_INTERVAL)