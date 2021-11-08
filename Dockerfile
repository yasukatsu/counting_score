FROM python:3

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install pandas cerberus
