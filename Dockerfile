FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY . /app
WORKDIR /app/src

RUN pip3 install requests==2.26.0

ENV APP_MODULE="main:app"
