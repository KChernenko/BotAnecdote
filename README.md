## BotAnecdote
Just a dump Telegram bot, which provides a random anecdote.

### How to build:

First of all, you'll need to create own bot through the Telegram's **@BotFather** - it will generate an API key,
which needs to be placed in the **config.py** file.

Bot depends on **gTTS** (Google Text-To-Speech) and **pyTelegramBotAPI** (Python Telegram API wrapper) libraries:

So, you need to install these dependencies through the **pip**.

`$ pip install gTTS`

And then:

`$ pip install pyTelegramBotAPI`

When everything is ready, just hit:

`$ python bot.py`

Enjoy.