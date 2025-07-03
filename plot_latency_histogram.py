import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the generated delay log
df = pd.read_csv("simulated_delay_log.csv")

# Set seaborn style
sns.set(style="whitegrid")

# Create histogram with KDE curve
plt.figure(figsize=(10, 6))
sns.histplot(
    data=df,
    x='latency_ms',
    hue='server_id',
    bins=30,
    kde=True,
    palette='pastel',
    edgecolor='black',
    stat='count'
)

# Styling
plt.title("Latency Distribution Histogram (Log-normal)", fontsize=14)
plt.xlabel("Latency (ms)", fontsize=12)
plt.ylabel("Task Count", fontsize=12)
plt.legend(title="Server ID")
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
