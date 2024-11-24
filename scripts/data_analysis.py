import pandas as pd
import matplotlib.pyplot as plt

def analyze_traffic_data(file_path):
    """Analyzes traffic noise data."""
    data = pd.read_csv(file_path)
    print(data.describe())
    data.plot(x='Time', y='Decibel', kind='line')
    plt.title("Traffic Noise Over Time")
    plt.xlabel("Time")
    plt.ylabel("Decibel (dB)")
    plt.show()

if __name__ == "__main__":
    analyze_traffic_data("data/traffic_data.csv")
