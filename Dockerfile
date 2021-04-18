FROM python:3.9-alpine


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE celta_news.settings.local


RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add zlib libjpeg-turbo-dev libpng-dev freetype-dev \
    && apk add lcms2-dev libwebp-dev harfbuzz-dev gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev \
    && apk add fribidi-dev tcl-dev tk-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && pip install pillow \
    && apk del build-deps


RUN mkdir /celta_news

WORKDIR /celta_news

ADD . /celta_news/

RUN pip install -r requirements.txt
