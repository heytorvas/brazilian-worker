FROM node:18.14

WORKDIR /app

RUN apt-get update && apt-get install -y \
    bsdutils=1:2.36.1-8+deb11u2 \
    curl=7.74.0-1.3+deb11u11 \
    imagemagick-6-common=8:6.9.11.60+dfsg-1.3+deb11u3 \
    imagemagick-6.q16=8:6.9.11.60+dfsg-1.3+deb11u3 \
    imagemagick=8:6.9.11.60+dfsg-1.3+deb11u3 \
    libaom0=1.0.0.errata1-3+deb11u1 \
    libapr1=1.7.0-6+deb11u2 \
    libblkid-dev=2.36.1-8+deb11u2 \
    libblkid1=2.36.1-8+deb11u2 \
    libc-bin=2.31-13+deb11u10 \
    libc-dev-bin=2.31-13+deb11u10 \
    libc6-dev=2.31-13+deb11u10 \
    libc6=2.31-13+deb11u10 \
    libcurl3-gnutls=7.74.0-1.3+deb11u11 \
    libde265-0=1.0.11-0+deb11u3 \
    libglib2.0-0=2.66.8-1+deb11u1 \
    libglib2.0-bin=2.66.8-1+deb11u1 \
    libglib2.0-data=2.66.8-1+deb11u1 \
    libglib2.0-dev-bin=2.66.8-1+deb11u1 \
    libglib2.0-dev=2.66.8-1+deb11u1 \
    libmount-dev=2.36.1-8+deb11u2 \
    libmount1=2.36.1-8+deb11u2 \
    libnghttp2-14=1.43.0-1+deb11u1 \
    libpq5=13.14-0+deb11u1 \
    libsmartcols1=2.36.1-8+deb11u2 \
    libssl-dev=1.1.1n-0+deb11u5 \
    libssl1.1=1.1.1n-0+deb11u5 \
    libtinfo6=6.2+20201114-2+deb11u2 \
    libx11-6=2:1.7.2-1+deb11u2 \
    libx11-data=2:1.7.2-1+deb11u2 \
    linux-libc-dev=5.10.218-1 \
    mount=2.36.1-8+deb11u2 \
    ncurses-base=6.2+20201114-2+deb11u2 \
    ncurses-bin=6.2+20201114-2+deb11u2 \
    openssh-client=1:8.4p1-5+deb11u3 \
    openssl=1.1.1n-0+deb11u5 \
    perl=5.32.1-4+deb11u3 \
    util-linux=2.36.1-8+deb11u2 \
    uuid-dev=2.36.1-8+deb11u2

COPY package*.json ./

RUN npm install

COPY . .
EXPOSE 4200

CMD npm start
