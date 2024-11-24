from scipy.signal import find_peaks
import numpy as np

def detect_siren(audio_signal):
    """Detect siren frequencies in an audio signal."""
    frequency = np.fft.fft(audio_signal)
    peaks, _ = find_peaks(np.abs(frequency), height=10)
    siren_detected = any(1000 < peak < 2000 for peak in peaks)
    return siren_detected

if __name__ == "__main__":
    sample_audio_signal = np.random.rand(1000)
    if detect_siren(sample_audio_signal):
        print("Siren detected!")
    else:
        print("No siren detected.")
