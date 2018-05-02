# -*- coding: utf-8 -*-
import os
import random

import telebot
from gtts import gTTS

import config
import persist

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["joke"])
def repeat_all_messages(message):
    text = random.choice(persist.jokes)
    filename = "synthesized" + str(random.randint(1, 1000)) + ".mp3"
    tts = gTTS(text=text, lang='ru')
    tts.save(filename)
    bot.send_audio(message.chat.id, open(filename, 'rb'))
    os.remove(filename)


if __name__ == '__main__':
    bot.polling(none_stop=True)
