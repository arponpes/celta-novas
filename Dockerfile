FROM python:3.9-buster


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE celta_news.settings.local


RUN apt-get update && apt-get install -y gcc python3-dev musl-dev libpng-dev libwebp-dev gcc libc-dev musl-dev tcl-dev tk-dev
RUN pip install psycopg2
RUN pip install pillow


RUN mkdir /celta_news
RUN mkdir -p /var/logs/django/

WORKDIR /celta_news

ADD . /celta_news/

RUN pip install -r requirements.txt
