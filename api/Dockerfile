FROM python:3.9

RUN mkdir /home/api
WORKDIR /home/api

COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000