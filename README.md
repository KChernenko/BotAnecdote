## BotAnecdote
Just a dump Telegram bot, which provides a random anecdote.

### How to build:

Python version : 3.6.5

First of all, you'll need to create own bot through the Telegram's **@BotFather** - it will generate an API key,
which needs to be placed in the **config.py** file.

Bot depends on **gTTS** (Google Text-To-Speech) and **pyTelegramBotAPI** (Python Telegram API wrapper), **requests** (Simple HttpClient) and **lxml** (XML\HTML parser and traverser) libraries:

So, you need to install these dependencies through the **pip**.

`$ pip3 install gTTS`

And then:

`$ pip3 install pyTelegramBotAPI`

When everything is ready, just hit:

`$ python3 bot.py`

Also, all of the dependencies are mentiones in **requirements.txt**

Enjoy.
