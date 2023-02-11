FROM python:3.9

RUN apt-get update && apt-get install -y \
    libmariadb-dev=1:10.5.18-0+deb11u1 \
    mariadb-common=1:10.5.18-0+deb11u1 \
    libtasn1-6=4.16.0-2+deb11u1 \
    linux-libc-dev=5.10.162-1 \
    libksba8=1.5.0-3+deb11u2 \
    libssl-dev=1.1.1n-0+deb11u4 \
    openssl=1.1.1n-0+deb11u4 \
    libde265-0=1.0.11-0+deb11u1

RUN mkdir /home/api
WORKDIR /home/api

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000
