# pull official base image
FROM python:3.11-slim-buster

# set working directory
WORKDIR /usr/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean


# add app
COPY . .

# install poetry
RUN pip install poetry

# install poetry
RUN poetry install --no-root

CMD ["poetry", "shell"]
