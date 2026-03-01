import os
from rembg import remove
from PIL import Image

def remove_backgrounds(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    print(f"Starting background removal. Reading from '{input_folder}'...")

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            
            # Change the output extension to .png to support transparency
            output_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_folder, output_filename)
            
            print(f"Processing: {filename} -> {output_filename}")
            
            try:
                # Open the image
                input_image = Image.open(input_path)
                
                # Remove the background using rembg
                output_image = remove(input_image)
                
                # Save the new transparent image
                output_image.save(output_path)
                print(f"  ✓ Success!")
            except Exception as e:
                print(f"  X Error processing {filename}: {e}")

    print("All done! Your transparent monsters are ready.")

# Set your folder paths here
input_dir = "monsters_input"
output_dir = "monsters_ready"

remove_backgrounds(input_dir, output_dir)