import json
import os

import requests
from urllib3 import request

from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = os.getenv('BOT_TOKEN')



CHAT_ID = os.getenv("CHAT_ID")

def sendMessage():
    try:
        url_text = 'http://api.forismatic.com/api/1.0/'
        data = {'method': 'getQuote', 'format': 'text', 'lang': 'ru'}
        citata = requests.post(url_text, data=data).text

        msg = f"{citata}\n<a href='https://pourlabeaute.ru/calendar/jdut-podtvergdeniy'>Новая запись</a>"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=HTML&text={msg}"
        print(requests.get(url).json())
    except:
        print('error')





