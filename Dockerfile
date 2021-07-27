# Defines base image
FROM python:3.9.5-alpine

# Set the working directory inside the container
WORKDIR /usr/src/app

# Set environment variables 
# Prevents copying Python pyc files to the container.
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures Python output is logged out to the terminal.
ENV PYTHONUNBUFFERED 1 

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# Copies project code 
COPY . /usr/src/app

# Expose port 8000 so the app can be accessed
# This EXPOSE is a redundant
EXPOSE 8000

# Runs the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
