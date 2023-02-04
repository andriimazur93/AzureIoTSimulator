FROM python:3.8-slim-buster

ENV SLEEP_INTERVAL_SECONDS=5
ENV MESSAGE_COUNT=100
ENV AZURE_CONN_STRING="ENTER_YOUR_CONNECTION_STRING_HERE" 

COPY requirements.txt /app/requirements.txt
COPY send_message.py /app/send_message.py

RUN pip install -r /app/requirements.txt

WORKDIR /app

CMD [ "python","-u", "send_message.py" ]
