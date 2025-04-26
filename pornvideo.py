import yt_dlp
import os
import requests
from pyrogram import Client
import time

yarrami_ye = 27833866  
ramowlf = "3648a12e9a8df3f448d4aeaac2ab91ab"  
baci_siken = "token gir"  
anne_hoplatan = "@sikisdeneme"

buraya_dokunma = "https://gist.githubusercontent.com/card2006/04bb99a18393885681077840b933952b/raw/d1998a8b4bfa4c8d6195444e4902ef6aad62f233/TIRI%2520MARRANO%2520SOLO%2520ADULTOS%2520+18%2520M3U"

ramazan_ozturk = set()
ramazan_abi = set()

ramo_ramazan = Client("ramobuba_session", api_id=yarrami_ye, api_hash=ramowlf, bot_token=baci_siken)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

def ramazanin_yarra():
    global ramazan_ozturk
    try:
        response = requests.get(buraya_dokunma, headers=headers, verify=False, timeout=10)
        if response.status_code == 200:
            yeni_ramo = [line.strip() for line in response.text.split("\n") if line.strip() and not line.startswith("#EXTINF")]
            yeni_ramo = [line for line in yeni_ramo if line.startswith("http")]
            kari_siken = set(yeni_ramo) - ramazan_ozturk
            ramazan_ozturk = set(yeni_ramo)
            return kari_siken
        return set()
    except Exception as e:
        print(f"Hata oldu aq: {e}")
        return set()

def ramowlf(ramazan):
    if ramazan in ramazan_abi:
        print(f"Zaten gönderildi: {ramazan}")
        return

    ramobuba = "ramo_baba.mp4"

    if os.path.exists(ramobuba):
        os.remove(ramobuba)

    try:
        print(f"İndiriliyor: {ramazan}")
        ydl_opts = {
            'outtmpl': ramobuba,
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'noplaylist': True,
            'quiet': False,
            'http_headers': {
                'User-Agent': headers["User-Agent"]
            }
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ramazan])

        ramo_ramazan.send_video(chat_id=anne_hoplatan, video=ramobuba, caption="sikiş videosu")
        ramazan_abi.add(ramazan)

    except Exception as e:
        print(f"İndirirken ya da gönderirken sıçtık: {e}")

def ramazani_doner_gibi_don():
    with ramo_ramazan:
        while True:
            try:
                yeni_linkler = ramazanin_yarra()
                for ramazan in yeni_linkler:
                    ramowlf(ramazan)
                time.sleep(60)
            except Exception as e:
                print(f"Loop hatası: {e}")
                time.sleep(10)

ramazani_doner_gibi_don()
