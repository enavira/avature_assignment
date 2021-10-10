FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY . /app
WORKDIR /app/src

RUN pip3 install requests==2.26.0

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
