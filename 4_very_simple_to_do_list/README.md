# Çok Basit Bir To-Do List Uygulaması

Bu proje, kullanıcıların görev ekleyebileceği, görüntüleyebileceği ve silebileceği interaktif bir Python tabanlı komut satırı To-Do List uygulamasıdır. Liste işlemleri, girdi işlemleri ve kontrol akışı gibi temel Python fonksiyonlarını öğrenmek için harika bir başlangıç noktasıdır.

---

## Proje Yapısı

- **Repository Adı**: `python`
- **Klasör Adı**: `4_very_simple_to_do_list`
- **Dosya Adı**: `app.py`

---

## Özellikler

1. **Görev Listesini Görüntüle**:

   - To-Do listesindeki mevcut görevleri görüntüler.

2. **Görev Ekle**:

   - Listeye yeni bir görev ekler.

3. **Görev Sil**:

   - Listeden belirli bir sıradaki görevi siler.

4. **Çıkış**:
   - Uygulamadan güvenli bir şekilde çıkış yapar.

---

## Script Nasıl Çalıştırılır?

1. Bu repository'i klonlayın:

   ```bash
   git clone <repository-url>
   ```

2. Proje klasörüne gidin:

   ```bash
   cd python/4_very_simple_to_do_list
   ```

3. Script'i çalıştırmak için şu komutu kullanın:
   ```bash
   python app.py
   ```

---

## Kullanım Talimatları

Script'i çalıştırdığınızda bir menü sunulacaktır. Menüdeki seçenekleri takip ederek To-Do listesi ile etkileşimde bulunabilirsiniz.

### Menü Seçenekleri:

- **1 - Görev Listesini Görüntüle**:
  Mevcut görev listesini gösterir. Eğer liste boşsa, herhangi bir görev görüntülenmez.

- **2 - Görev Ekle**:
  Eklenecek görevin açıklamasını girmenizi ister. Görev listeye eklenir.

- **3 - Görev Sil**:
  Silmek istediğiniz görevin sıra numarasını girmenizi ister. Seçilen görev listeden kaldırılır.

- **4 - Çıkış**:
  Uygulamayı kapatır.

### Örnek Kullanım:

```plaintext
1-Gorev Listesini Goruntule
2-Gorev Ekle
3-Gorev Sil
4-Cikis
Seciminiz: 2
Gorevi giriniz: Kitap okumayı bitir

1-Gorev Listesini Goruntule
2-Gorev Ekle
3-Gorev Sil
4-Cikis
Seciminiz: 1
TO-DO-LIST :
1. Kitap okumayı bitir

1-Gorev Listesini Goruntule
2-Gorev Ekle
3-Gorev Sil
4-Cikis
Seciminiz: 3
Kacinci gorevi silmek istiyorsunuz: 1

1-Gorev Listesini Goruntule
2-Gorev Ekle
3-Gorev Sil
4-Cikis
Seciminiz: 1
TO-DO-LIST :
```

---

## Hata Yönetimi

- Uygulama, geçersiz menü seçildiğinde bir hata mesajı göstererek kullanıcıyı bilgilendirir.
- Geçersiz bir sıra numarası girilerek görev silinmeye çalışıldığında bir hata oluşabilir. Bunun önüne geçmek için girilen numaranın mevcut listede yer aldığından emin olunmalıdır.

---

## Geliştirme Önerileri

İleri seviye geliştirme için şu özellikler eklenebilir:

1. **Girdi Doğrulama**:

   - Görev silme işlemi için geçerli indeks aralığını kontrol eden doğrulama eklenebilir.

2. **Kalıcı Depolama**:

   - To-Do listesi bir dosyaya (örneğin JSON, metin dosyası ya da veritabanı) kaydedilip yüklenebilir.

3. **Gelişmiş Arayüz**:

   - Daha etkileşimli bir komut satırı arayüzü için `curses` veya `rich` gibi kütüphaneler kullanılabilir.

4. **Görev Önceliklendirme**:

   - Görevlere öncelik atama özelliği eklenebilir.

5. **Grafik Arayüz**:
   - Tkinter veya PyQt gibi çerçeveler kullanılarak grafiksel bir arayüz geliştirilebilir.

---

## Lisans

Bu proje açık kaynaklıdır ve MIT Lisansı ile sunulmaktadır.

---

## Yazar

Bu proje bir Python meraklısı tarafından oluşturulmuştur. Katkı ve geri bildirimler memnuniyetle karşılanır!
