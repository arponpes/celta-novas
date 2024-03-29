FROM python:3.11-buster


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE celta_novas.settings.production


RUN mkdir /celta_novas
RUN mkdir -p /var/logs/django/
RUN mkdir /celta_novas/staticfiles

WORKDIR /celta_novas

ADD . /celta_novas/

RUN pip install -r base.txt


# Define the entry point script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entry point to execute necessary commands
ENTRYPOINT ["/entrypoint.sh"]
