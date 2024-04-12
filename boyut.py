import cv2

def dusur(giris_dosyasi):
    # Video yakalayıcı oluşturma
    video = cv2.VideoCapture(giris_dosyasi)

    # Çözünürlük ayarları
    yeni_genislik = 1280
    yeni_yukseklik = 720

    cikis_dosyasi = "1_" + giris_dosyasi

    # Video yazıcı oluşturma
    fps = video.get(cv2.CAP_PROP_FPS)
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    cozunurluk = (yeni_genislik, yeni_yukseklik)
    video_yazici = cv2.VideoWriter(cikis_dosyasi, codec, fps, cozunurluk)

    while True:
        ret, frame = video.read()

        if not ret:
            break

        # Çerçeveyi yeniden boyutlandırma
        frame = cv2.resize(frame, cozunurluk, interpolation=cv2.INTER_LINEAR)

        # Çerçeveyi videoya yazma
        video_yazici.write(frame)

    # Kaynakları serbest bırakma
    video.release()
    video_yazici.release()

    print("Boyut düşürüldü")
    return cikis_dosyasi
