import qrcode
import os

def split_base64_content(file_path, chunk_size):
    with open(file_path, 'r') as file:
        content = file.read()
    return [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]

def generate_qr_codes(file_path, output_directory, chunk_size=2800):
    chunks = split_base64_content(file_path, chunk_size)
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for index, chunk in enumerate(chunks):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(chunk)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        img_path = os.path.join(output_directory, f"qr_code_{index}.png")
        img.save(img_path)
        print(f"Saved QR code {index + 1} to {img_path}")

# Example usage:
# generate_qr_codes('path_to_your_base64_file.txt', 'output_directory_for_qr_codes')
