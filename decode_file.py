import os
import lzma
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# File decompression function
def decompress_with_lzma(input_file, output_file):
    with lzma.open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        f_out.writelines(f_in)

def decode_and_decrypt_aes_ctr(input_file, output_file, key, nonce):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
    decryptor = cipher.decryptor()
    with open(input_file, 'r') as f:
        encoded_data = f.read()
        encrypted_data = base64.b64decode(encoded_data.encode('utf-8'))
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

def decode_file(encoded_data_path, output_path, key, nonce):
    temp_decoded_path = 'temp_decoded.lzma'
    decode_and_decrypt_aes_ctr(encoded_data_path, temp_decoded_path, key, nonce)
    decompress_with_lzma(temp_decoded_path, output_path)

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
    decode_file(encoded_data_path, output_path, key, nonce)
    print(f"[+] Decoded file saved as {output_path}")
