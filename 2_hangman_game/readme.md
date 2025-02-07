# Adam Asmaca Oyunu

Bu Python programı, klasik bir kelime tahmin oyunu olan "Adam Asmaca"yı (Hangman) canlandırır. Oyuncu, gizli kelimeyi tahmin etmeye çalışırken sınırlı sayıda hata yapma hakkına sahiptir.

## Özellikler

1. **Kelime Seçimi:**

   - Program, `hangman_words` dosyasındaki kelime listesinden rastgele bir kelime seçer.

2. **Adam Asmaca Sanatı:**

   - Her yanlış tahminde, `hangman_art` dosyasındaki ASCII sanatını kullanarak oyuncunun kalan haklarını görselleştirir.

3. **Dinamik Ekran:**

   - Oyuncunun doğru ve yanlış tahminlerine göre kelimenin durumu güncellenir.

4. **Tekrar Tahmin Kontrolü:**

   - Oyuncu, daha önce tahmin ettiği bir harfi tekrar seçerse bilgilendirilir.

5. **Kazanma veya Kaybetme Durumu:**
   - Oyuncu tüm harfleri doğru tahmin ettiğinde oyunu kazanır.
   - Yanlış tahmin hakkı tükendiğinde oyunu kaybeder ve doğru kelimeyi görür.

## Nasıl Çalışır?

1. Program başlatıldığında bir logo görüntülenir.
2. `hangman_words` dosyasından bir kelime seçilir.
3. Seçilen kelimenin uzunluğuna göre boş çizgiler oluşturulur.
4. Oyuncudan bir harf tahmin etmesi istenir:
   - Doğru tahminde, harf yerleştirilir.
   - Yanlış tahminde, bir hak kaybedilir ve ASCII sanatı güncellenir.
5. Oyun şu durumlarda sona erer:
   - Oyuncu kelimenin tamamını doğru tahmin eder.
   - Oyuncunun hakları t t\u00fkenir.

## Örnek Kullanım

```plaintext
_ _ _ _ _
Guess a letter: a
Your letter is not in the word.
Your letter = a
 _____
|     |
|     O
|
|
|
_ _ _ _ _
Guess a letter: e
_ _ e _ _
```

## Gereksinimler

- Python 3.x
- `hangman_words` ve `hangman_art` modülleri:
  - `hangman_words.py` içinde kelime listesi bulunmalıdır.
  - `hangman_art.py` içinde ASCII sanat eserleri ve logo bulunmalıdır.

## Nasıl Çalıştırılır?

1. Reposu klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/hangman-game.git
   ```
2. Proje dizinine geçin:
   ```bash
   cd hangman-game
   ```
3. Programı çalıştırın:
   ```bash
   python hangman.py
   ```

## Notlar

- Oyuncu doğru tahmin etmeden önce seçilen kelime gösterilmeyecek şekilde düzenlenebilir (`print(chosen_word)` kaldırılabilir).
- ASCII sanat görselleri ve kelime listesi, `hangman_art.py` ve `hangman_words.py` dosyalarında özelleştirilebilir.

## Lisans

Bu proje açık kaynaklıdır ve [MIT Lisansı](LICENSE) kapsamında sunulmaktadır.

---

Sorularınız veya katkılarınız için iletişime geçmekten çekinmeyin!
