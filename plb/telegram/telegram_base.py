
import requests


from .input import BOT_TOKEN, CHAT_ID


BOT_TOKEN = BOT_TOKEN



CHAT_ID = CHAT_ID

def sendMessage():

    msg = "Привет! У тебя новая запись!"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    print(requests.get(url).json())



