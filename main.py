# main.py

from analog_encrypt import digital_to_analog, fme_encryption
from digital_encrypt import aes_encryption
from transmit import transmit_packets
from receive import receive_packets
from analog_decrypt import fme_decryption
from digital_decrypt import aes_decryption

# Function to generate a random message for testing
def generate_random_message(length=16):
    import random
    import string
    message = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    print(f"Original message: {message}")
    return message

# Main execution starts here
if __name__ == "__main__":
    # Generate random message for testing
    message = generate_random_message()

    # Step 1: Convert the message to analog signal
    analog_signal = digital_to_analog(message)

    # Step 2: Encrypt the analog signal using FME
    fme_encrypted_signal = fme_encryption(analog_signal)

    # Step 3: Encrypt the message using AES
    aes_key, aes_encrypted_signal = aes_encryption(message)

    # Step 4: Simulate transmitting the encrypted signals (both FME and AES)
    transmitted_fme_signal = transmit_packets(fme_encrypted_signal, packet_size=1000, drop_probability=0.2)
    transmitted_aes_signal = transmit_packets(aes_encrypted_signal, packet_size=1000, drop_probability=0.2)

    # Step 5: Reassemble the received signals
    received_fme_signal = receive_packets(transmitted_fme_signal, len(fme_encrypted_signal))
    received_aes_signal = receive_packets(transmitted_aes_signal, len(aes_encrypted_signal))

    # Step 6: Decrypt the received signals
    decrypted_fme_message = fme_decryption(received_fme_signal)
    decrypted_aes_message = aes_decryption(received_aes_signal, aes_key)

    # Print the decrypted messages
    print(f"Decrypted FME message: {decrypted_fme_message}")
    print(f"Decrypted AES message: {decrypted_aes_message}")

