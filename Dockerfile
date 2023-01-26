FROM python:3.7.16-slim-bullseye

COPY . /tmp

WORKDIR /tmp

RUN apt-get update

RUN apt install libpq-dev --yes

RUN pip install -r requirement.txt

ENTRYPOINT ["manage.py"] 