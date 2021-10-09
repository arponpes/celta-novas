FROM python:3.10-buster


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE celta_novas.settings.local


RUN mkdir /celta_novas
RUN mkdir -p /var/logs/django/

WORKDIR /celta_novas

ADD . /celta_novas/

RUN pip install -r requirements.txt
