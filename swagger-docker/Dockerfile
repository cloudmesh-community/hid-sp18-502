FROM mongo:latest
EXPOSE 27017
FROM ubuntu:16.04
#FROM python:3-alpine 
MAINTAINER Ankita Alshi <aralshi@iu.edu>

RUN apt-get update -q && apt-get install -qy \
    build-essential \
    python-dev \
    python-pip \
    #libssl-dev \
    zlib1g-dev \
    #libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    #pandoc \
    wget \
    curl \
    #emacs \
    git-core \
    default-jre \
    software-properties-common -y

#RUN apt-get update -q && apt-get install -qy default-jre 
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN apt-get update
RUN apt-get install -y mongodb
RUN mkdir /data
RUN mkdir /data/db
RUN chmod 777 /data/*
RUN pip install pymongo


RUN git clone https://github.com/cloudmesh-community/hid-sp18-502.git

WORKDIR /hid-sp18-502/swagger-docker

RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar

EXPOSE 8080

COPY mongod.conf /etc
RUN mkdir -p /var/lib/mongodb
CMD ["mongod", "-f", "/etc/mongod.conf"] 

RUN make service

CMD ["make", "start"]

