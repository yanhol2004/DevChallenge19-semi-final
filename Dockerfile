FROM python:3.9

COPY ./task/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./task /code/app
COPY ./key.pem /code/key.pem
COPY ./cert.pem /code/cert.pem

WORKDIR /code/app
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080", "--ssl-keyfile", "../key.pem", "--ssl-certfile", "../cert.pem"]

