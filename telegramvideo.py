import asyncio
from telegram import Bot
from telegram import InputFile
import requests

BOT_TOKEN = 'TOKEN_BURAYA_YAZ'

chat_id = 'CHAT_ID_BURAYA_YAZ'


def gonder(video):
    global BOT_TOKEN
    global chat_id
    # Telegram Bot'u oluşturma
    bot = Bot(token=BOT_TOKEN)

    # Gönderilecek resmin dosya yolu
    video_dosya_yolu = video  # Göndermek istediğiniz resmin dosya yolunu güncelleyin

    async def video_gonder():
        try:
            with open(video_dosya_yolu, 'rb') as video:
                await bot.send_video(chat_id=chat_id, video=InputFile(video))
            print("Video gönderildi")
            return True
        except Exception as e:
            print("Video gönderimi başarısız oldu:", e)
            return False

    # Asenkron fonksiyonu çalıştırma
    return asyncio.run(video_gonder())

def mesaj(zaman):
	
	global BOT_TOKEN
	global chat_id
	
	telegram_mesaj = f"Hareket Algılandı!\nGeçerli Zaman: {zaman}"
	url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
	params = {
	    'chat_id': chat_id,
	    'text': telegram_mesaj
	}
	response = requests.get(url, params=params)
	if response.status_code != 200:
	    print(f"Telegram'a mesaj gönderilemedi. {response.text}")
