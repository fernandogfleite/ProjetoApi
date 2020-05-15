FROM python:slim-buster

ENV APP /app

RUN mkdir $APP

WORKDIR $APP

RUN pip install flask flask-jsonpify flask-sqlalchemy flask-restful

RUN export FLASK_APP=hello.py

COPY . $APP