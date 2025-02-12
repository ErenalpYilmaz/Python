# 🃏 Blackjack Game

Bu proje, Python kullanarak Blackjack oyununu iki farklı yöntemle uygulayan bir projedir. Oyun, **dictionary** (sözlük) ve **list** (liste) veri yapıları kullanılarak iki farklı şekilde kodlanmıştır.

## 📌 Proje Yapısı

Bu proje, `python` adlı bir GitHub reposunun içinde bulunan `6_blackjack` klasöründe yer almaktadır. Klasörün içeriği aşağıdaki gibidir:

```
6_blackjack/
│── art.py                      # ASCII sanatı içeren dosya (logo)
│── blackjack_using_dictionary.py  # Dictionary kullanarak blackjack oyunu
│── blackjack_using_list.py        # List kullanarak blackjack oyunu
│── README.md                   # Proje dokümantasyonu
```

## 🎯 Amaç

Bu projede amaç, **Blackjack oyununun temel mekaniklerini** anlamak ve Python programlama dilini kullanarak iki farklı veri yapısıyla oyunu kodlamaktır.

---

## 🛠 Kullanılan Yöntemler

### 1️⃣ Dictionary ile Blackjack (`blackjack_using_dictionary.py`)

- **Dictionary** veri yapısı kullanılarak oyuncuların (kullanıcı ve bilgisayar) elleri bir sözlük içinde tutulur.
- Oyuncuların ve bilgisayarın kartlarını saklamak için `{ "user1": [...], "computer": [...] }` formatında bir sözlük kullanılmıştır.
- Oyun başladığında her oyuncuya iki kart dağıtılır.
- Oyuncu ek kart çekebilir veya oyunu bırakabilir.
- Bilgisayarın kart toplamı **17'den küçükse** otomatik olarak yeni kart çeker.
- **Kazananı belirlemek için skorlar karşılaştırılır.**

### 2️⃣ Liste ile Blackjack (`blackjack_using_list.py`)

- **List** veri yapısı kullanılarak oyuncuların kartları bir liste içinde tutulur.
- Oyuncunun ve bilgisayarın elleri ayrı listelerde saklanır (`user_cards`, `computer_cards`).
- Oyun başladığında her oyuncuya iki kart dağıtılır.
- Oyuncu ek kart çekebilir veya oyunu bırakabilir.
- Bilgisayarın kart toplamı **17'den küçükse** otomatik olarak yeni kart çeker.
- **Blackjack kontrolü** yapılarak anında kazanan belirlenebilir.
- **Oyun sonuçları** `compare()` fonksiyonu ile değerlendirilir.

---

## 🚀 Nasıl Çalıştırılır?

1. **Gerekli bağımlılıkları yükleyin (Eğer yoksa)**

   ```sh
   pip install -r requirements.txt  # (Bu proje için ekstra bir bağımlılık bulunmamaktadır)
   ```

2. **Projeyi çalıştırmak için aşağıdaki komutları kullanabilirsiniz:**

   - **Dictionary kullanarak blackjack:**
     ```sh
     python blackjack_using_dictionary.py
     ```
   - **Liste kullanarak blackjack:**
     ```sh
     python blackjack_using_list.py
     ```

3. **Oyunu oynamak için** terminale gelen talimatları takip edin.

---

## 🎲 Oyun Kuralları

- Her oyuncu başlangıçta **iki kart** alır.
- Oyuncunun toplam kart değeri **21’i geçerse kaybeder.**
- **As (A) kartı** 11 olarak değerlendirilir, ancak toplamı **21'i aşarsa 1 olarak değiştirilebilir.**
- **Bilgisayarın eli 17'den düşükse** otomatik olarak kart çeker.
- Skorlar hesaplanır ve kazanan belirlenir.

---

## 📌 Kazanan Nasıl Belirlenir?

Kazanan `compare()` fonksiyonu tarafından belirlenir:

- **Blackjack olması için 21 puan ve 2 kart  geldiğinde otomatik kazanır.**
- **Beraberlik olması durumunda** oyun "Draw" olarak sonuçlanır.
- **Oyuncunun skoru 21'i aşarsa** otomatik olarak kaybeder.
- **Bilgisayarın skoru 21'i aşarsa** oyuncu kazanır.

---

## 📜 Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır. İstediğiniz gibi kullanabilirsiniz. 😊

## 📞 İletişim

Eğer herhangi bir sorun yaşarsanız veya geliştirme önerileriniz varsa benimle iletişime geçebilirsiniz. 🚀

---

**👨‍💻 Herkese oyunda iyi eğlenceler dilerim. 🃏**
