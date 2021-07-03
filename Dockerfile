# syntax=docker/dockerfile:1
FROM python:3.9.5-slim-buster

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

WORKDIR /app

# Copy project files into docker container
COPY main.py main.py
COPY src/ src/

RUN mkdir ./data

# Python Modules Install
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Update Application Environment Variables
ENV PORT 4000
ENV ENVIRONMENT DOCKER
ENV DATA_DIR /app/data

CMD python main.py