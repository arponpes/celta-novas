FROM python:3.9-buster


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE celta_news.settings.local


RUN mkdir /celta_news
RUN mkdir -p /var/logs/django/

WORKDIR /celta_news

ADD . /celta_news/

RUN pip install -r requirements.txt
