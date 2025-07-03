import matplotlib.pyplot as plt

def plot_latency_distribution(tasks):
    latencies = [t.latency for t in tasks]
    plt.hist(latencies, bins=10, color='steelblue')
    plt.title("Latency Distribution")
    plt.xlabel("Latency (ms)")
    plt.ylabel("Number of Tasks")
    plt.grid(True)
    plt.show()