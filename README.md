# Hava Kirliliği Görüntü İşleme ve Model Performansı Karşılaştırma Projesi

Bu proje, fabrika kaynaklı ve motorlu taşıt kaynaklı hava kirliliği ile ilgili görüntülerin toplanması, işlenmesi, veri artırma ve çeşitli derin öğrenme modelleri ile sınıflandırılmasını kapsamaktadır. Proje kapsamında, toplama ve ön işleme aşamalarına ek olarak Vision Transformer (ViT), DeiT, BEiT, EfficientNet ve Swin Transformer modelleri ile performans karşılaştırması yapılmıştır.

---

## Proje Özeti
- **Konu:** Fabrika ve motorlu taşıtlardan kaynaklanan hava kirliliği görselleri.
- **Amaç:**
  1. Görüntülerin sınıflandırılması için yapay zeka modellerine uygun veri seti oluşturmak.
  2. Modellerin performansını karşılaştırıp en etkili modeli belirlemek.
- **Kapsam:**
  1. Görüntülerin toplanması, ön işlenmesi (parlaklık ve kontrast ayarı) ve veri artırma işlemleri.
  2. Modellerin ölçütlere göre karşılaştırılması.

---

## Kullanılan Teknolojiler ve Kütüphaneler

### Veri Toplama ve İşleme
- **Programlama Dili:** Python
- **Kütüphaneler:**
  - `selenium`: Görüntülerin web üzerinden otomatik olarak toplanması.
  - `Pillow (PIL)`: Görüntü işleme (parlaklık, kontrast ayarı ve döndürme).
  - `os`: Dosya ve klasör işlemleri.
  - `urllib`: Görüntülerin indirilmesi.

### Model Geliştirme ve Karşılaştırma
- **Derin Öğrenme Kütüphaneleri:**
  - `PyTorch`
  - `TensorFlow`
  - `HuggingFace Transformers`
- **Veri işleme:**
  - `scikit-learn`
  - `matplotlib`
  - `numpy`

---

## Proje Yapısı

### Klasörler
- **Veri Toplama ve İşleme:**
  - `downloaded_images, downloaded_images_2`: Toplanan ham görseller.
  - `yeni_parlaklik, yeni_parlaklik_2`: Parlaklık ayarı yapılmış görseller.
  - `yeni_kontrast, yeni_kontrast_2`: Kontrast ayarı yapılmış görseller.
  - `90derece, 90derece_2`: 90 derece döndürülmüş görseller.
- **Modeller ve Sonuçlar:**
  - `models/`: Kaydedilen model ağırlıkları.
  - `results/`: ROC eğrileri, karmaşıklık matrisleri ve model performans grafikleri.

### Python Scriptleri
1. **Görsel Toplama:**
   Web'den fabrika ve motorlu taşıt kaynaklı hava kirliliği görsellerini toplamak için `selenium` kullanılmıştır.
2. **Parlaklık Ayarı:**
   Görüntülerin parlaklığı `Pillow` kullanılarak %30 artırılmış ve yeni klasöre kaydedilmiştir.
3. **Kontrast Ayarı:**
   Görüntülerin kontrastı `Pillow` kullanılarak %40 artırılmış ve yeni klasöre kaydedilmiştir.
4. **Döndürme İşlemi:**
   Görüntüler 90 derece sola döndürülerek veri artırma işlemi yapılmıştır.
5. **Model Eğitimi:**
   Derin öğrenme modellerinin (ViT, DeiT, BEiT, EfficientNet, Swin Transformer) eğitilmesi ve performansının değerlendirilmesi.

---

## Model Performansı Karşılaştırması

| Model            | Accuracy | Precision | Recall | F1-Score | Sensitivity | Specificity | AUC  |
| ---------------- | -------- | --------- | ------ | -------- | ----------- | ----------- | ---- |
| **ViT**          | 99%      | 0.99      | 0.99   | 0.99     | 0.98        | 0.99        | 0.99 |
| **DeiT**         | 99%      | 0.99      | 0.99   | 0.99     | 0.99        | 0.99        | 0.99 |
| **BEiT**         | 98%      | 0.98      | 0.98   | 0.98     | 0.98        | 0.98        | 0.98 |
| **EfficientNet** | 99%      | 1.00      | 0.99   | 0.99     | 0.99        | 0.99        | 0.99 |
| **Swin**         | 98%      | 0.98      | 0.98   | 0.98     | 0.98        | 0.98        | 0.98 |

### ROC Eğrileri, Karmaşıklık Matrisleri ve Epoch Loss Grafikleri
SWİN Roc Grafiği: 
![swinroc](https://github.com/user-attachments/assets/938e669f-0ece-4bcc-898a-130d14fec5ac)


Swin Karmaşıklık Matrisi: 
![swinkarmasiklik](https://github.com/user-attachments/assets/8050605d-234d-44f2-8212-5ac5957597ac)


Swin Epoch Loss Grafiği: 
![swinepochloss](https://github.com/user-attachments/assets/cee6de13-5b6f-4134-93b1-838b07809850)


Efficiennet Roc Grafiği: 
![efficiennetrocgrafik](https://github.com/user-attachments/assets/d37ef397-788b-4094-8a22-9e39115f64fb)


Efficiennet Karmaşıklık Matrisi: 
![efficiennetkarmasiklik](https://github.com/user-attachments/assets/af1929c1-b3f4-46c4-9040-893d61fdbe37)


Efficiennet Epoch Loss Grafiği: 
![efficiennetepocloss](https://github.com/user-attachments/assets/5384dad4-068a-4037-9f33-17c2fa3d4604)


DeiT Roc Grafiği: 
![deit rocgrafik](https://github.com/user-attachments/assets/43db1667-1d7b-47ab-b70c-d7f237fa532c)


DeiT Karmaşıklık Matrisi: 
![deit karmasşıklık](https://github.com/user-attachments/assets/99b5bcb1-d056-4235-9a28-044a303b0de7)


DeiT Epoch Loss Grafiği: 
![deit epoclos](https://github.com/user-attachments/assets/e5f375f7-b751-4e22-80d1-1199f0056e59)


BEİT Roc Grafiği: 
![beitrocgrafik](https://github.com/user-attachments/assets/8ae86ac8-ec05-48ab-8351-584a3f21d301)


BEİT Karmaşıklık Matrisi: 
![beitkarmasik](https://github.com/user-attachments/assets/886e8247-6b7f-4e08-b84d-03726ef8a3e1)


BEİT Epoch Loss Grafiği: 
![beitepoclos](https://github.com/user-attachments/assets/d3d48c7f-5c2a-4e79-afa4-8c56fb74bc3e)


VİT Roc Grafiği: 
![vitrocgrafik](https://github.com/user-attachments/assets/745ed7a8-891d-460b-9b7b-a887b149862b)


BİT Karmaşıklık Matrisi: 
![vit karmaşıklık](https://github.com/user-attachments/assets/02481827-373b-46ab-ae78-ded10916c19e)


VİT Epoch Loss Grafiği: 
![vit eğitimtablosu](https://github.com/user-attachments/assets/a7582838-e9f8-4f73-b917-54831da6eec9)



---

## Nasıl Kullanılır?
1. **Gerekli Kütüphaneleri Kurun:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Görselleri Toplayın:**
   ```bash
   python goruntu_toplama.py
   ```
3. **Veri İşleme Scriptlerini Çalıştırın:**
   - Parlaklık: `python parlaklik_ayari.py`
   - Kontrast: `python kontrast_ayari.py`
   - Döndürme: `python dondurme.py`
4. **Modelleri Eğitin:**
   ```bash
   Colab Linkinden Projeye Ulaşabilirsiniz.
   ```
5. **Sonuçları ve Performansı Değerlendirin.**

---

## Sonuç
EfficientNet modeli, performans ve hesaplama etkinliği bakımından en iyi sonucu vermiştir. Proje, hava kirliliği izleme sistemleri için etkili bir yaklaşım sunmaktadır.
