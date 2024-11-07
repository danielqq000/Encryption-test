# analog_decrypt.py

import numpy as np
from scipy.signal import find_peaks
import math

# FME Decryption
def fme_decryption(modulated_signal, sample_rate=1000, modulation_index=10, duration=1):
    # Step 1: Extract frequencies from the modulated signal
    t = np.linspace(0, duration, len(modulated_signal))
    
    # Use peak detection to find frequencies from the modulated signal
    peaks, _ = find_peaks(modulated_signal, height=0)  # Adjust 'height' parameter as needed for your signal
    
    # Extract frequency based on the distance between peaks
    frequencies = []
    for i in range(1, len(peaks)):
        # Find the frequency between peaks
        period = peaks[i] - peaks[i-1]
        freq = sample_rate / period  # Frequency = Sample rate / period (time between peaks)
        frequencies.append(freq)
    
    # Step 2: Map the frequencies back to characters
    decoded_message = ""
    for freq in frequencies:
        # Map the frequency back to a character based on the original encoding logic
        # We assume the original encoding used the frequency as `ord(char) + 100`
        char_code = int(freq) - 100  # Reverse the encoding logic
        decoded_message += chr(char_code)
    
    return decoded_message
