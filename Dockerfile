FROM python:3.10.5-alpine3.16
WORKDIR /usr/src/bot
COPY . /usr/src/bot
RUN pip install --pre -r /usr/src/bot/requirements.txt
