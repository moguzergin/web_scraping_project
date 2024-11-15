from PIL import Image, ImageEnhance
import os

input_folder = "downloaded_images_2"
output_folder = "yeni_parlaklik_2"

brightness_factor = 1.3

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        img_path = os.path.join(input_folder, filename)

        with Image.open(img_path) as img:
            enhancer = ImageEnhance.Brightness(img)
            img_enhanced = enhancer.enhance(brightness_factor)

            output_path = os.path.join(output_folder, f"bright_{filename}")
            img_enhanced.save(output_path)
            print(f"{filename} parlaklık ayarı yapıldı ve {output_folder} klasörüne kaydedildi.")
