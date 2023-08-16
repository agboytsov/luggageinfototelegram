import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#loading secrets
load_dotenv()

flight = os.environ['FLIGHT']
surname = os.environ['SURNAME']

token = os.environ['TOKEN']

# Getting to Air Serbia luggage service. I suppose is can also be used not only for Air Serbia.
def get_status() -> str:
    """Searches for luggage information for lost&found luggage for Air Serbia"""

    browser = webdriver.Chrome()
    browser.get('http://www.worldtracer.aero/cgi-bin/filerequest.exe')

    elem = browser.find_element(By.XPATH, '//*[@id="record__reference"]')
    elem.send_keys(flight)
    elem = browser.find_element(By.XPATH, '//*[@id="skname__paxnameinternet"]')
    elem.send_keys(surname + Keys.RETURN)

    status = browser.find_element(By.XPATH, '/html/body/table/tbody/tr/td/div/table/tbody/tr['
                                            '3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/form/div/table/tbody/tr[4]/td/table/tbody/tr/td[2]/div/strong')

    return status.text


# Running the telegram bot that will answer with an information about the luggage on any messege (except /start,
# some kind of echo-bot:-))

#The bot uses aiogram, but this is shooting on pidgins from the cannon.

bot: Bot = Bot(token=token)
dp: Dispatcher = Dispatcher()


# "/start" command handling
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Hi! Nihao! Privet! Send my any message and I will check about your baggage')



# Answer with the info about luggage
@dp.message()
async def send_echo(message: Message):
    reply = get_status()

    await message.reply(text=reply)

# running bot
if __name__ == "__main__":
    dp.run_polling(bot)
