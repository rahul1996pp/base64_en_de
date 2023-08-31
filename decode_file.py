import os
import lzma
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def decode_decrypt_decompress(encoded_data, key, nonce):
    """Decode, decrypt, and decompress the given data."""
    # Base64 decoding
    encrypted_data = base64.b64decode(encoded_data.encode('utf-8'))
    # Decryption
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    # Decompression
    decompressed_data = lzma.decompress(decrypted_data)
    return decompressed_data

if __name__ == "__main__":
    # encoded_data_path = input("[+] Enter the path to the encoded data file: ").replace('"','')
    # output_path = input("[+] Enter the desired path for the decoded file: ").replace('"','')
    # key_hex = input("[+] Enter the key in hex format: ")
    # nonce_hex = input("[+] Enter the nonce in hex format: ")
    encoded_data_path = 'enc.txt'   # paste all encoded data
    output_path = 'test.zip'    # default
    encrypt_key = '293da84f509c0ef5d91471480dfde1f3d7ef0a71e1aee3dfb14ed9729f28db62:a1e435afffb9bc307df257b562b59e3e'  # paste _qr_key_nonce
    key_hex , nonce_hex = encrypt_key.split(":")
    key = bytes.fromhex(key_hex)
    nonce = bytes.fromhex(nonce_hex)
    with open(encoded_data_path, 'r') as f:
        encoded_data = f.read()
    decoded_data = decode_decrypt_decompress(encoded_data, key, nonce)
    with open(output_path, 'wb') as f:
        f.write(decoded_data)
    print(f"[+] Decoded file saved as {output_path}")
