FROM node:16-alpine

RUN mkdir /client

WORKDIR /client

ENV CHOKIDAR_USEPOLLING=true

RUN apk update && \
  apk add --no-cache python3 make g++ && \
  apk add git && \
  npm install -g npm@latest &\
  npm update -g yarn

COPY package.json .
COPY yarn.lock .

RUN yarn install
