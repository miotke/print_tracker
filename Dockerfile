# Defines base image
FROM python:3.9.5-alpine

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copies project code 
COPY . /usr/src/app
COPY ./requirements.txt /usr/src/app

# Set environment variables 
# Prevents copying Python pyc files to the container.
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures Python output is logged out to the terminal.
ENV PYTHONUNBUFFERED 1 

# Install dependencies
# Install postgres client 
RUN apk add --update --no-cache postgresql-client 

# Installs only certain OS dependencies so that the container is not bloated. 
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

# Installs app dependencies 
RUN pip install -r requirements.txt

# Remove temp files
RUN apk del .tmp-build-deps
