FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    samtools \
    tabix \
    python \
    python-pip \
    r-base \
    libcurl4-openssl-dev \
    wget \
    gzip

RUN R -q -e "setRepositories(graphics = FALSE, ind = 1:6); install.packages(\"sequenza\")"
RUN pip install sequenza-utils
RUN wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/phase2_reference_assembly_sequence/hs37d5.fa.gz && gunzip hs37d5.fa.gz

