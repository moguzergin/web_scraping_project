from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from PIL import Image
import time
import urllib.request
import os
from selenium.webdriver.chrome.options import Options

chrome_driver_path = r"C:\Users\ergin\OneDrive\Masaüstü\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=chrome_driver_path)

options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=service, options=options)

search_query = "fumo da scarico del veicoło"

driver.get("https://www.google.com/imghp")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

k = 15

time.sleep(3)
for _ in range(2):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(3)

try:
    other_options = driver.find_element(By.CLASS_NAME, 'kQdGHd')
    other_options.click()
    time.sleep(2)
except Exception as e:
    print("Diğer seçenekler butonuna tıklanırken hata oluştu:", e)

remaining_scrolls = k - 2
for _ in range(remaining_scrolls):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(3)

target_resolution = (1024, 768)
download_folder = "downloaded_images_2"
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

existing_images = [f for f in os.listdir(download_folder) if f.endswith('.jpg')]
existing_image_count = len(existing_images)
print(f"Mevcut görsel sayısı: {existing_image_count}")

image_count = existing_image_count
images = driver.find_elements(By.CLASS_NAME, "H8Rx8c")

for img in images:
    if image_count >= 400 + existing_image_count:
        break
    try:

        img.click()

        time.sleep(1)
        high_res_img = driver.find_element(By.XPATH, '//*[@jsname="kn3ccd"]')

        img_url = high_res_img.get_attribute("src") or high_res_img.get_attribute("data-src")

        if img_url:
            temp_image_path = f"{download_folder}/temp_{image_count}.jpg"
            urllib.request.urlretrieve(img_url, temp_image_path)

            with Image.open(temp_image_path) as image:
                resized_image = image.resize(target_resolution,
                                             Image.LANCZOS)
                final_image_path = f"{download_folder}/air_pollution_{image_count}.jpg"
                resized_image.save(final_image_path)
                print(f"{image_count + 1}. görüntü indirildi ve {target_resolution} çözünürlüğünde kaydedildi.")

            os.remove(temp_image_path)
            image_count += 1



    except Exception as e:
        print("Bir hata oluştu:", e)

driver.quit()
