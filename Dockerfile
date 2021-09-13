FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/DRF_COMMENTS_DOCKER_TEST

RUN pip install --upgrade pip
COPY ./req.txt /usr/src/req.txt
RUN pip install -r /usr/src/req.txt

COPY . /usr/src/DRF_COMMENTS_DOCKER_TEST

EXPOSE 8000