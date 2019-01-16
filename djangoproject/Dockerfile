FROM python:3-alpine

WORKDIR /usr/app
RUN apk add --no-cache --virtual build-base python3-dev mariadb-dev mariadb-connector-c-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD python manage.py runserver 0.0.0.0:8000
