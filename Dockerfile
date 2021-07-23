# Defines base image
FROM python:3

# Set the working directory for the files to be copied to
WORKDIR /usr/src/app/

# Copies the files from the root dir to the WORKDIR
COPY . .

# Instsall dependencies
RUN pip install -r requirements.txt

# Expose port 8000 so the app can be accessed
EXPOSE 8000

# Runs the development server
CMD python manage.py runserver
