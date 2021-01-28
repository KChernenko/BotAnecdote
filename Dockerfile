FROM python:3.6-alpine

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY src/ /app
WORKDIR /app

CMD nohup python bot.py > log.txt 2>&1 &