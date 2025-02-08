# Sezar Şifreleme Programı

Bu Python programı, basit bir şifreleme yöntemi olan Sezar Şifreleme tekniğini uygular. Bu teknik, bir mesajdaki harfleri alfabede belirtilen bir sayı kadar kaydırarak şifreler veya çözer.

## Özellikler

1. **Şifreleme ve Şifre Çözme:**

   - Kullanıcılar mesajlarını şifrelemek (encode) veya çözmek (decode) için seçim yapabilir.

2. **Alfabetik Olmayan Karakterleri Korur:**

   - Mesajdaki sayılar, semboller veya boşluklar olduğu gibi korunur ve şifrelenmez.

3. **Tekrar Kullanım:**
   - Program, kullanıcı çıkmayı seçene kadar şifreleme veya çözme işlemini tekrar etmeye olanak tanır.

## Nasıl Çalışır?

1. Program, önce `art.py` dosyasından bir logo içe aktarır ve ekrana yazdırır (Bu dosyanın projede bulunduğundan emin olun).
2. Kullanıcıdan bir işlem seçmesi istenir: `encode` (şifreleme) veya `decode` (şifre çözme).
3. Kullanıcı, işlem yapmak istediği mesajı ve şifreleme için bir kaydırma değeri girer.
4. Program, kullanıcının seçimine göre mesajı işler:
   - Harfleri belirtilen miktarda kaydırır.
   - Alfabetik olmayan karakterleri korur.
5. Sonuç ekranda gösterilir ve kullanıcıya programı yeniden başlatmak isteyip istemediği sorulur.
6. Kullanıcı `hayır` yazarsa, program bir veda mesajıyla sonlanır.

## Örnek Kullanım

```plaintext
Şifrelemek için 'encode', çözmek için 'decode' yazın:
encode
Mesajınızı yazın:
merhaba dünya
Kaydırma numarasını yazın:
5
Şifrelenmiş sonuç: rjwmfef itşdf

Tekrar denemek istiyorsanız 'evet', çıkmak için 'hayır' yazın:
evet
Şifrelemek için 'encode', çözmek için 'decode' yazın:
decode
Mesajınızı yazın:
rjwmfef itşdf
Kaydırma numarasını yazın:
5
Çözülmüş sonuç: merhaba dünya

Tekrar denemek istiyorsanız 'evet', çıkmak için 'hayır' yazın:
hayır
Görüşmek üzere :D
```

## Gereksinimler

- Python 3.x
- `art.py` modülü (logonun doğru şekilde görüntülenmesi için, bu dosyanın script ile aynı dizinde olduğundan emin olun).

## Nasıl Çalıştırılır?

1. Reposu klonlayın:
   ```bash
   git clone https://github.com/ErenalpYilmaz/Python.git
   ```
2. Proje dizinine geçin:
   ```bash
   cd 1_caesarCipher
   ```
3. Programı çalıştırın:
   ```bash
   python caesarCipher.py
   ```

## Notlar

- `Kaydırma` değeri alfabe üzerinde döngüsel olarak işlem yapar. Örneğin, kaydırma 1 olduğunda 'z' harfi 'a' olur.
- Program büyük/küçük harf duyarlı değildir; tüm girişler küçük harfe dönüştürülür.
- `art.py` dosyasının mevcut olduğundan emin olun, aksi halde logo görüntülenmez.

## Lisans

Bu proje açık kaynaklıdır ve [MIT Lisansı](LICENSE) kapsamında sunulmaktadır.

---

Katkıda bulunmak veya sorun bildirmek isterseniz, lütfen bizimle iletişime geçin!
