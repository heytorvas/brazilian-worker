FROM node:18.14

RUN apt-get update && apt-get install -y \
    libde265-0=1.0.11-0+deb11u1 \
    libapr1=1.7.0-6+deb11u2 \
    libssl-dev=1.1.1n-0+deb11u5 \
    linux-libc-dev=5.10.179-1 \
    libncurses-dev=6.2+20201114-2+deb11u1 \
    libpq-dev=13.11-0+deb11u1 \
    libtinfo6=6.2+20201114-2+deb11u1 \
    libwebp-dev=0.6.1-2.1+deb11u1 \
    ncurses-bin=6.2+20201114-2+deb11u1 \
    ncurses-base=6.2+20201114-2+deb11u1 \
    openssl=1.1.1n-0+deb11u5

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .
EXPOSE 4200

CMD npm start