FROM ubuntu:20.04
LABEL maintainer="yuri"

ENV DEBIAN_FRONTEND noninteractive

ADD sources.list /etc/apt/

RUN apt-get -y update && \
    apt-get -y install --fix-missing \
        lib32gcc1 \
        libfontconfig \
        libfreetype6 \
        libglib2.0-0 \
        libsm6 \
        libssl-dev \
        libstdc++6 \
        libxext6 \
        libxrender1 \
        lsb-core \
        qt5-default \
        sudo \
        ipython3 \
        python3-dev \
        python3-pip \
        python3-distutils && \
    apt-get -qy clean autoremove && \
    rm -rf /var/lib/apt/lists/*  && \
    ln -s /usr/bin/python3 /usr/bin/python

ENV PATH=$PATH:/usr/local/python3/bin:/home/idauser/.local/bin

RUN useradd -p $(openssl passwd -1 pwmd) -d /home/idauser -m -U -G sudo idauser
RUN chown idauser:idauser /home/idauser

# install
WORKDIR /home/idauser
COPY . .
RUN chown -R idauser:idauser /home/idauser

USER idauser
RUN chmod +x install.sh && ./install.sh && rm install.sh
