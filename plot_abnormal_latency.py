import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the abnormal delay log
df = pd.read_csv("abnormal_delay_log.csv")

# Set seaborn style
sns.set(style="whitegrid")

# Histogram with KDE (Kernel Density Estimate)
plt.figure(figsize=(10, 6))
sns.histplot(
    data=df,
    x='latency_ms',
    hue='server_id',
    bins=40,
    kde=True,
    palette='deep',
    edgecolor='black',
    stat='count'
)

# Style the plot
plt.title("Abnormal Latency Distribution Histogram", fontsize=14)
plt.xlabel("Latency (ms)", fontsize=12)
plt.ylabel("Task Count", fontsize=12)
plt.legend(title="Server ID")
plt.grid(True)
plt.tight_layout()
plt.show()
