FROM python:3.9

RUN apt-get update && apt-get install -y \
    libtasn1-6=4.16.0-2+deb11u1 \
    libksba8=1.5.0-3+deb11u2 \
    libssl-dev=1.1.1n-0+deb11u5 \
    openssl=1.1.1n-0+deb11u5 \
    libde265-0=1.0.11-0+deb11u1 \
    git=1:2.30.2-1+deb11u2 \
    git-man=1:2.30.2-1+deb11u2 \
    libaprutil1=1.6.1-5+deb11u1 \
    libgnutls30=3.7.1-5+deb11u3 \
    libapr1=1.7.0-6+deb11u2

RUN mkdir /home/api
WORKDIR /home/api

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000
