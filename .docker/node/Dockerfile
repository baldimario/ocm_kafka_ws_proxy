FROM node:14-buster

RUN mkdir /ocm

WORKDIR /ocm

RUN npm install
RUN npm install -g wscat

CMD ["sh", "-c", "npm install && npm audit fix && node server.js"]
#CMD ["sh", "-c", "tail -f /dev/null"]
