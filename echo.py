"""import requests

API_link = "https://api.telegram.org/bot1268048580:AAF4imj0o0N7OC2ZIa4j9b1xtPwS-Tf_PNs"

updates = requests.get(API_link + "/getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]
chat_id = message["from"]["id"]
text = message["text"]

send_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Привет, ты написал {text}")

#
import asyncio
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
Markdown
Форматирование текста
<i>italic</i> курсив
<d>bold</b> жирный
dp = Dispatcher(bot, loop=loop)

if __name__=="__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)"""""