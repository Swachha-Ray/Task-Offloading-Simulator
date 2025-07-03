
from device import Device
from edge_server import EdgeServer
from scheduler import Scheduler
import pandas as pd
import matplotlib.pyplot as plt

def main():
    num_devices = 2
    tasks_per_device = 10
    edge_servers = [
        EdgeServer("A", cpu_power_ghz=4, bandwidth_mbps=50, delay_log_path="abnormal_delay_log.csv"),
        EdgeServer("B", cpu_power_ghz=5, bandwidth_mbps=100, delay_log_path="abnormal_delay_log.csv"),
    ]
    scheduler = Scheduler(policy="greedy")
    all_tasks = []
    task_log = []
    step = 0

    for i in range(num_devices):
        device = Device(device_id=f"D{i}", cpu_power_ghz=1.5, battery_level=100.0)
        device.generate_tasks(tasks_per_device)
        sorted_tasks = sorted(device.tasks, key=lambda t: t.priority)

        for task in sorted_tasks:
            assigned_task = scheduler.assign(task, device, edge_servers, step)
            all_tasks.append(assigned_task)
            task_log.append({
                "task_id": task.task_id,
                "latency_ms": task.latency,
                "deadline": task.deadline,
                "assigned": task.assigned,
                "priority": task.priority,
                "success": task.success,
                "battery_level": round(device.battery_level, 2)
            })
            step += 1

    df = pd.DataFrame(task_log)
    df.to_csv("task_log.csv", index=False)
    print(df.head())

    # Simple plot
    df['assigned'].value_counts().plot(kind='bar', title='Execution Type Count', color='orange')
    plt.ylabel("Number of Tasks")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
