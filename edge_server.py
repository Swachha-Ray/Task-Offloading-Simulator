import pandas as pd

class EdgeServer:
    def __init__(self, server_id, cpu_power_ghz, bandwidth_mbps, delay_log_path=None):
        self.server_id = server_id
        self.cpu_power = cpu_power_ghz
        self.bandwidth = bandwidth_mbps  # Mbps
        self.delay_log = None

        if delay_log_path:
            df = pd.read_csv(delay_log_path)
            self.delay_log = df[df['server_id'] == server_id].reset_index(drop=True)

    def get_current_latency(self, step):
        if self.delay_log is not None and step < len(self.delay_log):
            return self.delay_log.loc[step, 'latency_ms']
        else:
            return 20  # default fallback

    def execute(self, task, step):
        trans_time = (task.data_size * 8) / self.bandwidth * 1000  # ms
        comp_time = (task.cpu_cycles / (self.cpu_power * 1000))    # ms
        network_latency = self.get_current_latency(step)
        total_latency = network_latency + trans_time + comp_time
        task.assigned = f'edge-{self.server_id}'
        task.latency = round(total_latency, 2)
        task.success = task.latency <= task.deadline
        return task