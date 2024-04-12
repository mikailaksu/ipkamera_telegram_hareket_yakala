import cv2
from datetime import datetime
import telegramvideo
import os
import time
import boyut

print("Başladı")

# Silinecek dosyaların bulunduğu dizin
dizin = '.'

# Dizindeki dosyaları tarayarak .mp4 uzantısına sahip olanları silme
for dosya in os.listdir(dizin):
    if dosya.endswith('.mp4'):
        dosya_yolu = os.path.join(dizin, dosya)
        os.remove(dosya_yolu)

# IP kamera bağlantı bilgileri
kamera_ip = '192.168.1.50' # kamera ip güncelleyin
kamera_kullanici = 'admin'  # kullanıcı adını güncelleyin
kamera_sifre = '123456'  # şifreyi güncelleyin

# IP kamera bağlantısı
kamera_url = f'rtsp://{kamera_kullanici}:{kamera_sifre}@{kamera_ip}:554/ch01.264?dev=1' #rstp linki
video_akisi = cv2.VideoCapture(kamera_url)

# Kamera bağlantısının başarıyla gerçekleştiğini kontrol etme
if not video_akisi.isOpened():
    print(f"Kamera bağlantısı başarısız. {kamera_ip}")
else:
    print(f"Kameraya bağlandı {kamera_ip}")

# Hintergrund çerçevesi oluşturma
ret, arka_plan = video_akisi.read()

# Hintergrund çerçevesini griye dönüştürme
arka_plan_gri = cv2.cvtColor(arka_plan, cv2.COLOR_BGR2GRAY)
arka_plan_gri = cv2.GaussianBlur(arka_plan_gri, (21, 21), 0)

# Hareket algılandığında ekrana yazdırma ve video kaydetme
hareket_alglandi = False
kayit_yapiliyor = False
kayit_suresi = 0
kayit_maksimum_sure = 10  # Kayıt süresini isteğe bağlı olarak ayarlayabilirsiniz

# Video kaydetme için VideoWriter nesnesi oluşturma
codec = cv2.VideoWriter_fourcc(*'mp4v')
fps = 25
video_kaydedici = None

while True:
    # Kamera akışından bir çerçeve alıp işleme tabi tutma
    ret, cerceve = video_akisi.read()

    if not ret:
        print("Çerçeve alınamadı.")
        break

    # Hareket algılama için arka plan çerçevesi ile mevcut çerçeve arasındaki farkı hesaplama
    fark = cv2.absdiff(arka_plan, cerceve)

    # Fark görüntüsünü griye dönüştürme
    fark_gri = cv2.cvtColor(fark, cv2.COLOR_BGR2GRAY)
    fark_gri = cv2.GaussianBlur(fark_gri, (21, 21), 0)

    # Fark görüntüsünü eşikleme
    esik_degeri = 30  # Eşik değerini isteğe bağlı olarak ayarlayabilirsiniz
    _, eşik = cv2.threshold(fark_gri, esik_degeri, 255, cv2.THRESH_BINARY)

    # Eşikli görüntüdeki kontur noktalarını bulma
    konturlar, _ = cv2.findContours(eşik, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Hareket algılandığında ekrana yazdırma ve video kaydetme
    if len(konturlar) > 80 and not hareket_alglandi:
        print("Hareket Algılandı!")
        hareket_alglandi = True
        kayit_yapiliyor = True
        zaman = datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
        telegramvideo.mesaj(zaman)
        isim = f'hareket_video_{zaman}.mp4'
        video_kaydedici = cv2.VideoWriter(isim, codec, fps, (cerceve.shape[1], cerceve.shape[0]), isColor=True)

    if kayit_yapiliyor:
        kayit_suresi += 1
        video_kaydedici.write(cerceve)

        if kayit_suresi > kayit_maksimum_sure * fps:
            kayit_yapiliyor = False
            hareket_alglandi = False
            kayit_suresi = 0
            video_kaydedici.release()
            print("Kayıt tamamlandı!")
            yenisi = boyut.dusur(isim)
            if telegramvideo.gonder(yenisi):
                os.remove(isim)
                os.remove(yenisi)

# Kullanılan kaynakları serbest bırakma
video_akisi.release()
cv2.destroyAllWindows()
