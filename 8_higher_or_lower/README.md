# Higher or Lower Oyunu

```
                                 _   _  _         _                   _____         _
                                 | | | |(_)       | |                 |  _  |       | |
                                 | |_| | _   __ _ | |__    ___  _ __  | | | | _ __  | |      ___  __      __  ___  _ __
                                 |  _  || | / _` || '_ \  / _ \| '__| | | | || '__| | |     / _ \ \ \ /\ / / / _ \| '__|
                                 | | | || || (_| || | | ||  __/| |    \ \_/ /| |    | |____| (_) | \ V  V / |  __/| |
                                 \_| |_/|_| \__, ||_| |_| \___||_|     \___/ |_|    \_____/ \___/   \_/\_/   \___||_|
                                             __/ |
                                          |___/
```

Bu proje, **Higher or Lower** isimli popüler tahmin oyununu Python kullanarak oluşturduğum bir uygulamadır. Oyunun amacı, iki farklı ünlü veya markanın Instagram takipçi sayılarını karşılaştırarak daha fazla takipçiye sahip olanı doğru tahmin etmektir.

---

## 📌 Nasıl Çalışır?

1. Oyun başladığında rastgele iki hesap seçilir.
2. Kullanıcı, hangi hesabın daha fazla takipçiye sahip olduğunu tahmin eder.
3. Eğer doğru tahminde bulunursa, puanı artar ve oyun devam eder.
4. Yanlış tahminde bulunursa oyun sona erer ve final skoru ekrana yazdırılır.

---

## 📂 Proje Yapısı

Bu proje **Python** programlama diliyle geliştirilmiştir ve aşağıdaki dosya yapısına sahiptir:

```
python/
│── 8_higher_or_lower/
│   │── main.py         # Ana oyun dosyası
│   │── art.py          # ASCII sanatı içeren dosya (logo, vs. görselleri)
│   │── game_data.py    # Takipçi bilgileri içeren veri dosyası
│── README.md            # Ana proje README dosyası
```

---

## 🚀 Kullanım

1. **Projeyi klonlayın:**
   ```sh
   git clone https://github.com/ErenalpYilmaz/python.git
   ```
2. **Dizine gidin:**
   ```sh
   cd python/8_higher_or_lower
   ```
3. **Oyunu çalıştırın:**
   ```sh
   python main.py
   ```

---

## 📜 Kütüphaneler

Bu proje Python'un yerleşik `random` kütüphanesini kullanmaktadır. Harici bir bağımlılığı bulunmamaktadır.
