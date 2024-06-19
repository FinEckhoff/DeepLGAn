from PIL import Image
import os

def create_gif(image_folder, output_path, duration=500):
    # Get all image file paths from the specified folder
    images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif"))]
    images.sort()  # Sort the images by name, useful if they are named sequentially

    # Load images into a list
    frames = [Image.open(os.path.join(image_folder, img)) for img in images]

    # Ensure at least one image is loaded
    if not frames:
        raise ValueError("No images found in the provided directory")

    # Save as GIF
    frames[0].save(output_path, format='GIF', append_images=frames[1:], save_all=True, duration=duration, loop=0)

# Example usage
image_folder = '/home/fin_eckhoff/Projects/GAN/cpimages'
output_path = 'output.gif'
create_gif(image_folder, output_path, duration=500)