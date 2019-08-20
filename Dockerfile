FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    samtools \
    tabix \
    wget \
    python-pip \
    R
RUN pip install sequenza-utils
