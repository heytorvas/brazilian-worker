FROM node:18.14

RUN apt-get update && apt-get install -y \
    libde265-0=1.0.11-0+deb11u1 \
    libapr1=1.7.0-6+deb11u2

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .
EXPOSE 4200

CMD npm start