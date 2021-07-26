# Print Tracker 

A small Django application used to track my 3D prints and to learn how to use Docker and automate deployment. Deployment will be to a Raspberry Pi more than likely. 


## Docker 

All commands are documented as this is a learning project. Currently the database is build into the same image. The database will be removed from this image at a later time.

Docke Hub: https://hub.docker.com/repository/docker/andrewmiotke/print_tracker

### Build 

`docker build -t andrewmiotke/print_tracker .`

### Run 

`docker run -d -p 8000:8000 andrewmiotke/print_tracker`

This uses `-d` to run in detached mode and exposes the app to port 8000 using `-p`.
