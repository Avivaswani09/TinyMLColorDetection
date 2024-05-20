from PIL import Image, ImageDraw
import os
import numpy as np

# Set your dataset directory
dataset_dir = 'color_dataset'

# Create the dataset directory if it doesn't exist
os.makedirs(dataset_dir, exist_ok=True)

# Function to create a color block image with a given RGB value
def create_color_block(rgb, size=(100, 100)):
    image = Image.new('RGB', size, rgb)
    return image

# Function to save the image with its corresponding RGB value as filename
def save_image_with_label(image, rgb, index):
    filename = os.path.join(dataset_dir, f'{rgb[0]}_{rgb[1]}_{rgb[2]}.png')
    image.save(filename)

# Generate synthetic color block images with corresponding RGB values
num_images = 1000  # Adjust as needed

for i in range(num_images):
    # Generate random RGB values
    rgb = np.random.randint(0, 256, size=3)
    
    # Create color block image
    color_block_image = create_color_block(tuple(rgb))
    
    # Save image with corresponding RGB value as the filename
    save_image_with_label(color_block_image, rgb, i)
