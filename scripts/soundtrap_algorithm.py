import time
import random

def record_audio():
    """Simulates audio recording and returns decibel level."""
    return random.uniform(70, 100)  # Simulated dB value

def calculate_decibel(analog_signal):
    """Convert analog signal to decibel."""
    return 20 * (analog_signal ** 0.5)

def capture_video(vehicle_id):
    """Capture a 10-second video clip."""
    print(f"Captured video for vehicle ID {vehicle_id}")

def issue_challan(vehicle_id, decibel, location, timestamp):
    """Generate an e-challan for noise violation."""
    print(f"E-challan issued to {vehicle_id} for {decibel} dB at {location} on {timestamp}")

def soundtrap_process():
    """Main function simulating SoundTrap functionality."""
    while True:
        decibel = record_audio()
        if decibel > 80:  # Noise threshold
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            vehicle_id = f"Vehicle-{random.randint(1000, 9999)}"
            location = "Hyderabad Traffic Zone"
            capture_video(vehicle_id)
            issue_challan(vehicle_id, decibel, location, timestamp)
        time.sleep(5)

if __name__ == "__main__":
    soundtrap_process()
