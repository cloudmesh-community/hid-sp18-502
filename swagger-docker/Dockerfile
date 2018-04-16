FROM mongo:latest
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




RUN git clone https://github.com/cloudmesh-community/hid-sp18-502.git

WORKDIR /hid-sp18-502/swagger-docker

RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar

RUN mkdir -p /data/db 
EXPOSE 8080
EXPOSE 27017
VOLUME ["data/db"]

RUN make service

CMD ["make", "start"]

