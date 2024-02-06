FROM nginx:latest

RUN rm -fr /etc/nginx/conf.d/default.conf

COPY ./default.conf /etc/nginx/conf.d

RUN apt -y update

RUN apt install -y dnsutils net-tools inetutils-ping curl
