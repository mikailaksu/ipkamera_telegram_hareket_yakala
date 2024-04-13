# ipkamera_telegram_hareket_yakala
İp Kameraya üzerinde hareket olduğunda telegram'dan telefona video gönderir.

İp kameranız varsa ip adresini ve rstp bilgilerini girerek Bir hareket olduğunda telegramdan bir video alabilirsiniz!

![](https://i.hizliresim.com/1c0ir7q.jpg)

## Gerekenler

- Python 3 gereklidir.
- Bir Telegram botu oluşturun, Tokeninizi ve chatid anahtarlarını kaydedin.
- Kameralara göre RSTP LİNKİ DEĞİŞİKLİL GÖSTEREBİLİR. Bunun için [Onvif](https://sourceforge.net/projects/onvifdm/) üzerinden rstp bağlantınızı kontrol edin.

![](https://i.hizliresim.com/a22j5w0.jpg)

## _Ayarlar_

- hareket.py dosyası üzerine kameranıza ait ip adresi, username, password ve rstp linkini güncelleyin.
- telegramvideo.py üzerinden telegram bot tokeninizi ve chatid değerinizi güncelleyin.

 ## _Çalıştırma_

linux

 ```sh
pip install requirements.txt
python3 hareket.py
```

Windows

 ```sh
python -mpip install requirements.txt
python hareket.py
```

NOT: Linux kullanıyorsanız veya benim gibi raspberry üzerinde çalıştırıyor iseniz sistem her başladığında çalışması için crontab.txt içinde verdiğim kodu cronunuza ekleyerek sürekli çalışmasını sağlayabilirsiniz.

