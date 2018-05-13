# -*- coding: utf-8 -*-
import os
import re
import time

import requests
import telebot
from gtts import gTTS
from lxml import html

import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["joke"])
def repeat_all_messages(message):
    text = get_random_anekdot()
    filename = convert_text_to_voice_file(text)
    bot.send_audio(message.chat.id, open(filename, 'rb'))
    os.remove(filename)


def convert_text_to_voice_file(message):
    filename = re.sub(r"[\"-\,]", "", message)[:18]
    print(filename)
    tts = gTTS(text=message, lang='ru')
    tts.save(filename)
    return filename


def get_random_anekdot():
    url = "https://www.anekdot.ru/random/anekdot/"

    headers = {
        'Cache-Control': "no-cache",
        'User-Agent': "Mozilla/5.0 (Macintosh;"
    }

    response = requests.request("GET", url, headers=headers)

    tree = html.fromstring(response.content)
    anek_of_the_day = tree.xpath('//div[@class="topicbox"]/div[@class="text"]')
    return anek_of_the_day[0].text_content()


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)

        # An ugly hack to protect from HttpExceptions. We should probably use a Webhooks instead of LongPolling:
        # https://github.com/eternnoir/pyTelegramBotAPI/issues/241#issuecomment-284819864
        except Exception as e:
            time.sleep(15)
