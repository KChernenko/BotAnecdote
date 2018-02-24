# -*- coding: utf-8 -*-
import telebot

import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(func=lambda message: True, content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
