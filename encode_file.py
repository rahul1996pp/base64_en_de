import os
import lzma
import base64
import qrcode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Constants
MAX_QR_DATA_SIZE = 2500

def compress_encrypt_encode(input_file, key, nonce):
    """Compress, encrypt, and encode a given file."""
    with open(input_file, 'rb') as f:
        data = f.read()

    # Compression
    compressed_data = lzma.compress(data)

    # Encryption
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(compressed_data) + encryptor.finalize()

    # Base64 encoding
    encoded_data = base64.b64encode(encrypted_data).decode('utf-8')
    return encoded_data

def generate_qr_codes(data, original_path):
    """Generate QR codes for the given data and key+nonce."""
    base_dir = os.path.dirname(original_path)
    base_filename = os.path.splitext(os.path.basename(original_path))[0]

    # Key and nonce QR
    sequence = key.hex() + ':' + nonce.hex()
    key_nonce_qr_file_name = os.path.join(base_dir,output_dir,base_filename + "_qr_key_nonce.png")
    generate_qr(sequence, key_nonce_qr_file_name)

    # Data QRs
    chunks = [data[i:i+MAX_QR_DATA_SIZE] for i in range(0, len(data), MAX_QR_DATA_SIZE)]
    qr_file_paths = [key_nonce_qr_file_name]
    for index, chunk in enumerate(chunks):
        qr_file_name = os.path.join(base_dir,output_dir, base_filename + f"_qr_{index}.png")
        generate_qr(chunk, qr_file_name)
        qr_file_paths.append(qr_file_name)

    return qr_file_paths

def generate_qr(text, output_file):
    """Generate a QR code for the given text."""
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

if __name__ == "__main__":
    # Generate a random key and nonce for this demonstration
    key = os.urandom(32)
    nonce = os.urandom(16)
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    original_path = input("[+] Enter the path to the original file: ").replace('"','')
    encoded_data = compress_encrypt_encode(original_path, key, nonce)
    qr_files = generate_qr_codes(encoded_data, original_path)
    print(f"[+] Generated QR codes: {', '.join(qr_files)}")
