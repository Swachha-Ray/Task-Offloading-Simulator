
from task import Task

class Device:
    def __init__(self, device_id, cpu_power_ghz, battery_level=100.0):
        self.device_id = device_id
        self.cpu_power = cpu_power_ghz  # GHz
        self.battery_level = battery_level  # %

    def generate_tasks(self, num_tasks=10):
        self.tasks = [Task.generate_random() for _ in range(num_tasks)]

    def execute_locally(self, task):
        exec_time = (task.cpu_cycles / (self.cpu_power * 1000))  # ms
        energy_cost = 0.05 * exec_time  # Arbitrary
        self.battery_level -= energy_cost
        task.assigned = 'local'
        task.latency = round(exec_time, 2)
        task.success = task.latency <= task.deadline
        return task
