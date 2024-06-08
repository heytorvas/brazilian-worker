FROM python:3.9

WORKDIR /home/api

RUN apt-get update

RUN pip install pip==23.3

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
