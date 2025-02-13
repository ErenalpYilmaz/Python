# 7 Sayı Tahmin Oyunu

**7 Sayı Tahmin Oyunu**'na hoş geldiniz!  
Bu proje, kullanıcının 1 ile 100 arasında rastgele seçilen bir sayıyı tahmin etmesi gereken eğlenceli ve etkileşimli bir Python oyunudur. Oyun, **kolay** ve **zor** olmak üzere iki farklı zorluk seviyesi sunar. Seçilen zorluk seviyesine göre kullanıcının belirli sayıda deneme hakkı olur.

## 📌 İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Nasıl Oynanır?](#nasıl-oynanır)
- [Özellikler](#özellikler)
- [Gereksinimler](#gereksinimler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## 🎯 Proje Hakkında

Oyun, 1 ile 100 arasında rastgele bir sayı seçer. Kullanıcıdan bu sayıyı tahmin etmesi istenir ve her tahminden sonra aşağıdaki geri bildirimlerden biri verilir:

✅ **Doğru tahmin**: Oyuncu doğru tahmini yaparsa oyunu kazanır.  
⬆️ **Çok yüksek**: Kullanıcının tahmini, seçilen sayıdan büyüktür.  
⬇️ **Çok düşük**: Kullanıcının tahmini, seçilen sayıdan küçüktür.

Oyuncunun **zorluk seviyesine** bağlı olarak belirli sayıda tahmin hakkı bulunur:

- **Kolay:** 10 deneme hakkı
- **Zor:** 5 deneme hakkı

Kullanıcı, doğru tahmini yapamaz ve tüm haklarını bitirirse oyunu kaybeder.

## 🎮 Nasıl Oynanır?

1. **Zorluk Seviyesi Seçin:**

   - `'easy'` yazarak **10 tahmin hakkı** alabilirsiniz.
   - `'hard'` yazarak **5 tahmin hakkı** alabilirsiniz.

2. **Sayıyı Tahmin Edin:**

   - Zorluk seviyesini seçtikten sonra bir tahmin girin.
   - Oyun size tahmininizin çok **yüksek**, çok **düşük** veya **doğru** olup olmadığını söyleyecektir.

3. **Oyunun Sonucu:**
   - Sayıyı doğru tahmin ederseniz oyunu **kazanırsınız** 🎉
   - Tahmin hakkınız biterse **kaybedersiniz** ❌

## 🚀 Özellikler

✅ **Rastgele Sayı Üretimi:** Oyun, 1 ile 100 arasında rastgele bir sayı seçer.  
✅ **Zorluk Seviyeleri:** Kolay ve zor olmak üzere iki farklı oyun modu bulunmaktadır.  
✅ **Geri Bildirim Mekanizması:** Kullanıcıya yaptığı tahmine göre yönlendirme sağlanır.  
✅ **Deneme Sayacı:** Oyuncunun kaç tahmin hakkı kaldığını gösterir.

## 🛠 Gereksinimler

Bu projeyi çalıştırmak için bilgisayarınızda **Python 3.x** yüklü olmalıdır.

## 🔧 Kurulum

1. Bu repoyu bilgisayarınıza klonlayın:

```bash
git clone https://github.com/yourusername/python.git
```

2. Proje dizinine gidin:

```bash
cd 7_Number_Guessing_Project
```

## ▶️ Kullanım

Oyunu başlatmak için `main.py` dosyasını çalıştırın:

```bash
python main.py
```

Komut satırında oyunun yönergelerini takip ederek oynayabilirsiniz.

## 🤝 Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz:

- Yeni özellikler ekleyebilir,
- Hataları düzeltebilir,
- Daha iyi bir kullanıcı deneyimi için önerilerde bulunabilirsiniz.

Fork'layıp geliştirdiğiniz projeyi pull request olarak gönderebilirsiniz.

## 📜 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.
