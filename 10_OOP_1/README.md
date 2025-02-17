# ☕ Kahve Makinesi Projesi (OOP ile)

## Giriş
Bu proje, kullanıcıların kahve siparişi verebileceği, sanal para ile ödeme yapabileceği ve kaynakları yönetebileceği **Python tabanlı bir Kahve Makinesi** simülasyonudur. Proje, **Nesne Yönelimli Programlama (OOP)** prensiplerini, sınıf tasarımını, kapsüllemeyi ve modüler yapıyı göstermektedir.
## Bilgilendirme
- 9_CoffeeMachine klasöründeki kodlarla aynı mantıkta çalışmaktadır.Bu projenin amacı daha öncesinde methodlarla yaptığım projeyi OOP ile Class'lar aracılığı ile nasıl yapabileceğimi öğrenmek oldu.
- [Detaylı bilgi için `Coffe Machine README`](../9_CoffeeMachine/README.md)
## Özellikler
- 📚 **Nesne Yönelimli Tasarım**: Farklı işlevleri yöneten birden fazla sınıf kullanılarak yapılandırılmıştır.
- 🤖 **Etkileşimli Konsol Arayüzü**: Kullanıcılar komut satırını kullanarak kahve makinesi ile etkileşime girebilir.
- 💸 **Sanal Ödeme Sistemi**: Farklı madeni para türlerini kabul eder ve para üstünü hesaplar.
- ⚙️ **Kaynak Yönetimi**: Kullanılabilir su, süt ve kahve miktarlarını takip eder ve günceller.
- 📝 **Raporlama Sistemi**: Mevcut kaynakları ve kazanılan toplam parayı gösterir.

## Proje Yapısı
```plaintext
├── coffee_maker.py  # Kaynak yönetimi ve kahve yapımını kontrol eder
├── menu.py          # Menü öğelerini saklar ve içecek seçeneklerini listeler
├── money_machine.py # İşlemleri ve kâr takibini yönetir
├── main.py          # Kahve makinesi programını çalıştırır
```

## Sınıf İncelemesi
### 1. `MenuItem`
Bireysel kahve seçeneklerini, içeriklerini ve fiyatlarını temsil eder.

### 2. `Menu`
- Birden fazla `MenuItem` nesnesini saklar.
- Kullanılabilir içecekleri listeler ve belirli bir içeceği bulur.

### 3. `MoneyMachine`
- Ödeme işlemlerini yönetir.
- Madeni paraları işler ve para üstünü hesaplar.
- Toplam kârı takip eder.

### 4. `CoffeeMaker`
- Mevcut kaynakları (su, süt, kahve) yönetir.
- Siparişin yapılabilir olup olmadığını kontrol eder.
- Kahve yapıldığında kaynakları düşer.

## Projenin Çalıştırılması
1. Depoyu klonlayın:
   ```sh
   git clone https://github.com/ErenalpYilmaz/python.git
   ```
2. Proje dizinine gidin:
   ```sh
   cd python/10_OOP_1
   ```
3. Programı çalıştırın:
   ```sh
   python main.py
   ```

## Kullanım
- Bir kahve türü girin (`espresso`, `latte`, `cappuccino`) ve sipariş verin.
- **`report`** yazarak mevcut kaynakları kontrol edin.
- **`off`** yazarak makineyi kapatın.

## Örnek Etkileşim
```plaintext
What would you like? espresso/latte/cappuccino: latte
Please insert coins.
How many quarters?: 10
Here is $7.5 in change.
Here is your latte ☕️. Enjoy!
```

## Neden 2 Tane Aynı Proje Var?
Bu proje, **9_CoffeeMachine** projesinin bir kopyasıdır. Amacım, önceki versiyonda öğrendiğim bilgileri pekiştirmek, kodu optimize etmek ve daha iyi bir nesne yönelimli yapı oluşturmayı denemekti. Böylece, **OOP prensiplerini daha iyi anlamak ve geliştirmek** için aynı projeyi tekrar yaparak deneyimlerimi artırmış oldum.

## Gelecek Geliştirmeler
- 📊 Grafik Arayüz (GUI) tabanlı bir arayüz
- 🌐 Web tabanlı kahve sipariş sistemi
- 🎯 Gelişmiş hata yönetimi

---
❤️ ile geliştirildi: [Erenalp Yılmaz](https://github.com/ErenalpYilmaz)

