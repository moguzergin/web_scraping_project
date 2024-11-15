from PIL import Image, ImageEnhance
import os

# Girdi ve çıktı klasörlerini tanımlayın
input_folder = "downloaded_images_2"  # Orijinal görsellerin bulunduğu klasör
output_folder = "yeni_kontrast_2"  # Düzenlenmiş görsellerin kaydedileceği klasör

# Çıkış klasörünü oluşturun, eğer mevcut değilse
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Kontrast katsayısı (1.0 normal kontrast, 1.5 %50 artırılmış kontrast)
contrast_factor = 1.4  # Görsellerin kontrastını %40 artırma

# Tüm görseller üzerinde kontrast ayarını yap ve kaydet
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):  # .jpg formatındaki görselleri seç
        img_path = os.path.join(input_folder, filename)

        # Görseli aç ve kontrast ayarı yap
        with Image.open(img_path) as img:
            enhancer = ImageEnhance.Contrast(img)
            img_enhanced = enhancer.enhance(contrast_factor)

            # Yeni dosya adını belirleyip kaydet
            output_path = os.path.join(output_folder, f"contrast_{filename}")
            img_enhanced.save(output_path)
            print(f"{filename} kontrast ayarı yapıldı ve {output_folder} klasörüne kaydedildi.")
