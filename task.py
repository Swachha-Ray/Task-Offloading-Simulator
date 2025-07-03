
import random
import uuid

class Task:
    def __init__(self, cpu_cycles, data_size, deadline, priority=None):
        self.task_id = str(uuid.uuid4())[:8]
        self.cpu_cycles = cpu_cycles  # in MegaCycles
        self.data_size = data_size    # in MB
        self.deadline = deadline      # in ms
        self.priority = priority if priority is not None else random.choice([0, 1, 2])  # 0=High, 1=Medium, 2=Low
        self.assigned = None
        self.latency = None
        self.success = None

    @staticmethod
    def generate_random():
        return Task(
            cpu_cycles=random.randint(500, 3000),
            data_size=round(random.uniform(0.5, 5.0), 2),
            deadline=random.randint(50, 300)
        )
