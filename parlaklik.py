from PIL import Image
import os

input_folder = "downloaded_images_2"
output_folder = "90_derece_2"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        img_path = os.path.join(input_folder, filename)

        with Image.open(img_path) as img:
            img_rotated = img.rotate(90, expand=True)

            output_path = os.path.join(output_folder, f"rotated_{filename}")
            img_rotated.save(output_path)
            print(f"{filename} 90 derece sola döndürüldü ve {output_folder} klasörüne kaydedildi.")
