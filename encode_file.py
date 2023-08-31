import os
import lzma
import base64
import qrcode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Constants
MAX_QR_DATA_SIZE = 2500

# File compression and decompression functions
def compress_with_lzma(input_file, output_file):
    with open(input_file, 'rb') as f_in, lzma.open(output_file, 'wb') as f_out:
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

def generate_qr(text, output_file):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

def generate_qr_codes_after_encoding(data, original_path):
    base_dir = os.path.dirname(original_path)
    base_filename = os.path.splitext(os.path.basename(original_path))[0]  # Remove file extension
    sequence = key.hex() + ':' + nonce.hex()
    key_nonce_qr_file_name = os.path.join(base_dir,output_dir, base_filename + "_qr_key_nonce.png")
    generate_qr(sequence, key_nonce_qr_file_name)
    
    chunks = [data[i:i+MAX_QR_DATA_SIZE] for i in range(0, len(data), MAX_QR_DATA_SIZE)]
    qr_file_paths = [key_nonce_qr_file_name]
    for index, chunk in enumerate(chunks):
        qr_file_name = os.path.join(base_dir,output_dir, base_filename + f"_qr_{index}.png")
        generate_qr(chunk, qr_file_name)
        qr_file_paths.append(qr_file_name)
    return qr_file_paths

def encode_file(original_path):
    temp_compressed_path = 'temp_compressed.lzma'
    temp_encoded_path = 'temp_encoded.encoded'
    compress_with_lzma(original_path, temp_compressed_path)
    encrypt_and_encode_aes_ctr(temp_compressed_path, temp_encoded_path, key, nonce)
    with open(temp_encoded_path, 'r') as f:
        encoded_data = f.read()
    qr_files = generate_qr_codes_after_encoding(encoded_data, original_path)
    print(f"[+] Generated QR codes: {', '.join(qr_files)}")

if __name__ == "__main__":
    # Generate a random key and nonce for this demonstration
    key = os.urandom(32)
    nonce = os.urandom(16)
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    original_path = input("[+] Enter the path to the original file: ").replace('"','')
    # original_path=r""
    encode_file(original_path)
