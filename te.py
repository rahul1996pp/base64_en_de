import qrcode

def base64_to_qrcode(file_path, output_image_path):
    # Read the base64 encoded file
    with open(file_path, 'r') as file:
        encoded_string = file.read()
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(encoded_string)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save QR code as image
    img.save(output_image_path)

# Example usage:
# base64_to_qrcode('path_to_your_base64_file.txt', 'output_qrcode_image.png')
