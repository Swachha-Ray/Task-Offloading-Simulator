import pandas as pd
import numpy as np
import random

def generate_delay_data(distribution='normal', mean=30, std=5, count=1000, server_ids=['A', 'B']):
    data = []

    for step in range(count):
        for server_id in server_ids:
            if distribution == 'normal':
                latency = np.random.normal(loc=mean, scale=std)
            elif distribution == 'exponential':
                latency = np.random.exponential(scale=mean)
            elif distribution == 'uniform':
                latency = random.uniform(mean - std, mean + std)
            elif distribution == 'lognormal':
                latency = np.random.lognormal(mean=np.log(mean), sigma=0.4)
            else:
                raise ValueError("Unsupported distribution")

            latency = round(max(1, latency), 2)  # Avoid negatives or 0
            data.append({
                'timestamp_ms': step,
                'server_id': server_id,
                'latency_ms': latency
            })

    return pd.DataFrame(data)

# Usage Example:
if __name__ == "__main__":
    df = generate_delay_data(distribution='lognormal', mean=25, std=5, count=1000)
    df.to_csv("simulated_delay_log.csv", index=False)
    print("Generated delay log: simulated_delay_log.csv")