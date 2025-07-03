
class Scheduler:
    def __init__(self, policy="greedy"):
        self.policy = policy

    def assign(self, task, device, edge_servers, step=0):
        if self.policy == "greedy":
            local_task = device.execute_locally(task)
            if local_task.success:
                return local_task
            else:
                best_edge = min(edge_servers, key=lambda s: s.get_current_latency(step))
                return best_edge.execute(task, step, device)
        elif self.policy == "edge_only":
            best_edge = min(edge_servers, key=lambda s: s.get_current_latency(step))
            return best_edge.execute(task, step, device)
        elif self.policy == "random":
            import random
            if random.random() < 0.5:
                return device.execute_locally(task)
            else:
                return random.choice(edge_servers).execute(task, step, device)
        else:
            raise ValueError("Unknown policy")
