# Python Hesap Makinesi

```
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
```

Bu proje, Python ile yazılmış basit bir hesap makinesidir. Kullanıcıdan iki sayı alarak toplama, çıkarma, çarpma ve bölme işlemlerini gerçekleştirebilir. Kullanıcı, önce bir işlem seçer ve ardından sonucu görmek için hesaplamayı yapar. Hesaplama tamamlandıktan sonra, kullanıcı yeni bir işlem yapabilir veya devam eden hesaplamayı kullanarak işlem yapmaya devam edebilir.

## Özellikler

- **Dört işlem desteği:** Toplama (+), Çıkarma (-), Çarpma (\*), Bölme (/)
- **Sürekli hesaplama:** Kullanıcı sonucu bir sonraki işlemde kullanabilir.
- **Yeniden başlatma:** Kullanıcı hesaplamayı sıfırlayabilir veya programı sonlandırabilir.
- **Kullanıcı dostu arayüz:** Kullanıcıdan giriş alarak işlemleri yönlendiren basit ve etkili bir akış.
- **Sözlük kullanımı:** Tüm işlemler bir Python sözlüğü (`operations`) içine fonksiyonlar olarak eklenmiştir. Kullanıcı seçim yaptığında ilgili fonksiyon çalıştırılır.

## Kullanım

1. Projeyi klonlayın:

   ```sh
   git clone https://github.com/kullanici_adiniz/proje_adi.git
   cd proje_adi
   ```

2. Programı çalıştırın:

   ```sh
   python main.py
   ```

3. İlk olarak, kullanıcıdan bir sayı girmesi istenir.
4. Kullanıcı, işlem yapmak istediği operatörü seçer.
5. İkinci sayıyı girdikten sonra işlem gerçekleştirilir ve sonuç ekrana yazdırılır.
6. Kullanıcı **'y'** tuşuna basarak devam edebilir veya **'n'** tuşuna basarak yeni bir hesaplama başlatabilir.
7. **'quit'** komutu ile programdan çıkabilir.

## Örnek Kullanım

```
What's the first number?: 10
+
Pick an operation: +
What's the next number?: 5
10 + 5 = 15
Type 'y' to continue calculating with 15, type 'quit' to stop calculate, or type 'n' to start a new calculation: y
Pick an operation: *
What's the next number?: 2
15 * 2 = 30
Type 'y' to continue calculating with 30, type 'quit' to stop calculate, or type 'n' to start a new calculation: quit
```

## Gereksinimler

- Python 3.x
- `art.py` dosyası proje içinde bulunmalıdır (logo gösterimi için)

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına göz atabilirsiniz.

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir **pull request** gönderin veya bir **issue** açarak önerilerinizi paylaşın.
