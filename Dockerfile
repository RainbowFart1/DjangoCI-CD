FROM python:3.10
MAINTAINER Potato
ENV PYTHONUNBUFFERED 1
COPY pip.conf /root/.pip/pip.conf
RUN mkdir -p /home/Potato_Blog
WORKDIR /home/Potato_Blog
ADD . /home/Potato_Blog
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod +x ./start.sh
RUN chmod -R 777 ./start.sh
