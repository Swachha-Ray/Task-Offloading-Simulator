import pandas as pd
import numpy as np
import random

def generate_abnormal_delay_data(count=1000, server_ids=['A', 'B']):
    data = []

    for step in range(count):
        for server_id in server_ids:
            # Simulate normal latency with spikes every 100 steps
            if step % 100 == 0:
                latency = np.random.uniform(100, 200)  # spike
            elif random.random() < 0.1:
                latency = np.random.normal(loc=70, scale=15)  # jitter
            else:
                latency = np.random.normal(loc=30, scale=5)  # normal

            latency = round(max(5, latency), 2)
            data.append({
                'timestamp_ms': step,
                'server_id': server_id,
                'latency_ms': latency
            })

    return pd.DataFrame(data)

# Save to CSV
df_abnormal = generate_abnormal_delay_data()
df_abnormal.to_csv("abnormal_delay_log.csv", index=False)
print("Generated abnormal delay log: abnormal_delay_log.csv")
