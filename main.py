#
from telethon import *
import requests
import logging

from telethon import errors
WEB_HDRS = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',

    'Accept': 'text/html,text/plain,application/xhtml+xml,application/xml,application/_json;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Charset': 'Windows-1252,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8;q=0.5',
    'Connection': 'keep-alive'
}
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

API_KEY = "5031850285:AAFt56IwixuWnoL2dmGYjPKVNRXqU8JD6uc"
api_id = 7979686
api_hash = "72604998fe33dc2eb90cb37b64cfd2c5"
bot = TelegramClient("Bot", api_id, api_hash).start(bot_token=API_KEY)
deniz = 1144967052

def register(pattern):
    return bot.on(events.NewMessage(pattern=pattern))


@register(pattern="^/start")
async def start(event):
    await event.reply("Çalışıyor...")

@register(pattern="^asd")
async def get_adzan(event):
    if event.sender_id != deniz:
        return
    link = event.text.split()
    
    print(link)
    url = f"https://www.pnd.tl/api?api=90edf199f17aa2f2455d8d624cc524a097627291&url={link[-1]}&category=6"
    
    ksl = requests.get(url).json()
    ksl = ksl['shortenedUrl']
    sve = event.reply("Kısaltılıyor...")
    aciklama = " ".join(link[1:-1])
    #await sve.edit(f"{aciklama}\n\n❌ SILINMEDEN IZLE ❌\n\n👉 {ksl}\n\nLink nasıl açılır\n👉@linkk_gecmee")
    await sve.edit(f"{aciklama}\n\n📛 **SESİ AÇ** 'a tıklamayı unutma\n\n𝐋𝐢𝐍𝐊🔗 {ksl}\n\n❗️Link nasıl açılır\n👉 https://t.me/linkk_gecmee")
    #await sve.edit(f"{aciklama}\n\n👇DEVAMI LİNKTE👇\n\n𝐋𝐢𝐍𝐊🔗 {ksl}")

@register(pattern="^.post")
async def postitf(message):
    if message.sender_id != deniz:
        return
    yanitlanan_mesaj = await message.get_reply_message()
    count = 0
    mess = await message.reply("`Post gönderiliyor...`")
    for kanal in kanallar:
        try:
            if yanitlanan_mesaj.media:
                await message.client.send_file(kanal, file=yanitlanan_mesaj.media, caption=yanitlanan_mesaj.text)
            else:
                await message.client.send_message(kanal, yanitlanan_mesaj.text)
        except Exception as e:
            await mess.reply(f"Bir kanala post gönderilemedi!\n\n{e}\n\n{kanal}")
        else:
            count += 1
    await mess.edit(f"{count} `kanala post gönderildi.`")


logger.info("Bot Çalışıyor...")
bot.run_until_disconnected()
