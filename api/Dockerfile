FROM python:3.9

RUN apt-get update && apt-get install -y \
    libmariadb-dev=1:10.5.18-0+deb11u1 \
    mariadb-common=1:10.5.18-0+deb11u1 \
    libtasn1-6=4.16.0-2+deb11u1 \
    linux-libc-dev=5.10.162-1 \
    libksba8=1.5.0-3+deb11u2 \
    libssl-dev=1.1.1n-0+deb11u4 \
    openssl=1.1.1n-0+deb11u4 \
    libde265-0=1.0.11-0+deb11u1 \
    git=1:2.30.2-1+deb11u2 \
    git-man=1:2.30.2-1+deb11u2 \
    libaprutil1=1.6.1-5+deb11u1 \
    libgnutls30=3.7.1-5+deb11u3

RUN mkdir /home/api
WORKDIR /home/api

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000
