FROM ubuntu
RUN apt-get update && apt-get install -yq python python-pip vim build-essential python-dev libssl-dev libffi-dev
RUN easy_install PyOpenSSL twisted

