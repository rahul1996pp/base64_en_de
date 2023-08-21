from PIL import Image
import math

def file_to_bitmap(file_path, output_image_path):
    # 1. Read the file as a sequence of bytes
    with open(file_path, 'rb') as file:
        data = file.read()
    
    # 2. Convert each byte to a grayscale pixel value
    pixel_data = [byte for byte in data]
    
    # 3. Calculate the best rectangular dimensions for the image
    total_pixels = len(pixel_data)
    width = int(math.sqrt(total_pixels))
    height = total_pixels // width
    remaining_pixels = total_pixels - (width * height)
    
    # Handle any remaining pixels by adjusting width and height
    while remaining_pixels > 0:
        width += 1
        height = total_pixels // width
        remaining_pixels = total_pixels - (width * height)
    
    # 4. Create an image with these pixel values
    image = Image.new('L', (width, height))
    image.putdata(pixel_data)
    
    # 5. Save the image
    image.save(output_image_path)

# Example usage:
# file_to_bitmap('path_to_your_file', 'output_image.png')
