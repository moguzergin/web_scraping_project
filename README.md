# Hava Kirliliği Görüntü İşleme ve Veri Ön İşleme Projesi

Bu proje, fabrika kaynaklı ve motorlu taşıt kaynaklı hava kirliliği ile ilgili görüntülerin toplanması, işlenmesi ve sınıflandırılmasına yönelik veri hazırlama sürecini içermektedir. Proje kapsamında veriler toplanmış, parlaklık, kontrast ayarı yapılmış ve görüntüler işlenmiştir. Ayrıca, görseller döndürülerek veri artırma işlemleri gerçekleştirilmiştir.

## Proje Özeti
- **Konu:** Fabrika ve motorlu taşıtlardan kaynaklanan hava kirliliği görselleri.
- **Amaç:** Görüntülerin sınıflandırılması için yapay zeka modellerine uygun veri seti oluşturmak.
- **Kapsam:** Görsel verilerin toplanması, ön işlenmesi (parlaklık ve kontrast ayarı) ve veri artırma işlemleri.

---

## Kullanılan Teknolojiler ve Kütüphaneler
- **Programlama Dili:** Python
- **Kütüphaneler:**
  - `selenium`: Görsellerin web üzerinden otomatik olarak toplanması.
  - `Pillow (PIL)`: Görüntü işleme (parlaklık, kontrast ayarı ve döndürme).
  - `os`: Dosya ve klasör işlemleri.
  - `urllib`: Görsellerin indirilmesi.

---

## Proje Yapısı
### Klasörler
- `downloaded_images, downloaded_images_2`: Toplanan ham görseller.
- `yeni_parlaklik, yeni_parlaklik_2`: Parlaklık ayarı yapılmış görseller.
- `yeni_kontrast, yeni_kontrast_2`: Kontrast ayarı yapılmış görseller.
- `90derece, 90derece_2`: 90 derece döndürülmüş görseller.

### Python Scriptleri
1. **Görsel Toplama:**
   Web'den fabrika ve motorlu taşıt kaynaklı hava kirliliği görsellerini toplamak için `selenium` kullanılmıştır.
   
2. **Parlaklık Ayarı:**
   Görsellerin parlaklığı `Pillow` kullanılarak %30 artırılmış ve yeni klasöre kaydedilmiştir.

3. **Kontrast Ayarı:**
   Görsellerin kontrastı `Pillow` kullanılarak %40 artırılmış ve yeni klasöre kaydedilmiştir.

4. **Döndürme İşlemi:**
   Görseller 90 derece sola döndürülerek veri artırma işlemi yapılmıştır.

---

## Nasıl Kullanılır?
1. **Gerekli Kütüphaneleri Kurun:**
2. **Görselleri Toplayın:**
`görsel_toplama.py` scriptini çalıştırarak ham görselleri toplayın.
3. **Parlaklık Ayarını Yapın:**
`parlaklik_ayari.py` scriptini çalıştırarak görsellerin parlaklığını ayarlayın.
4. **Kontrast Ayarını Yapın:**
`kontrast_ayari.py` scriptini çalıştırarak görsellerin kontrastını ayarlayın.
5. **Döndürme İşlemini Yapın:**
`dondurme.py` scriptini çalıştırarak görselleri döndürün.
