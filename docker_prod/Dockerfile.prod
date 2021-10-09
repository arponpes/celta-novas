FROM python:3.10-buster


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE celta_novas.settings.production


RUN mkdir /celta_novas
RUN mkdir -p /var/logs/django/
RUN mkdir /celta_novas/staticfiles

WORKDIR /celta_novas

ADD . /celta_novas/

RUN pip install -r requirements.txt
