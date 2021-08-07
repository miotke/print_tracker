# Print Tracker 

A small Django application used to track my 3D prints and to learn how to use Docker and automate deployment. Deployment will be to a Raspberry Pi more than likely. 

## Docker 

All commands are documented as this is a learning project. Currently the database is build into the same image. The database will be removed from this image at a later time.

Docke Hub: https://hub.docker.com/repository/docker/andrewmiotke/print_tracker

### Docker Compose

You can run either `docker-compose` or `dockercompose`, both will have the same results.

#### Fresh install (zero data in database)
1. `docker-compose run app python manage.py makemigrations`
    - Shapes the Postgres database with the print_tracker model.
2. `docker-compose run app python manage.py migrate` 
    - Creates the Postgres database and establishes a connection with the app
3. `docker-compose run app python manage.py createsuperuser`
    - Allows you to create a Django superuser account
4. `docker-compose up`
    - Spins up all services allowing you to finally access the app. 

#### Existing install 

If the services(containers) are already built and the volume is established, simply run `docker-compose up` to bring up the containers and make the app accessible. Use `docker-compose down` to tear down all running services(containers).

#### Flags

- Use the `-d` flag to run it as a daemon, `docker-compose up -d`

### Build 

`docker build -t andrewmiotke/print_tracker .`

### Run 

`docker run -d -p 8000:8000 andrewmiotke/print_tracker`

This uses `-d` to run in detached mode and exposes the app to port 8000 using `-p`.

## Architecture

This section outlines the current Docker container and volume architecture for this app. 

### Services/Containers 

The docker-compose.yml file outlines two services, `app` and `database`, the two are fairly self-explanitory. By breaking the app and the database up into two different services(containers) the data inside the database should not be affected when a container is torn down and built back up. In instances were something changes on the app, the app container can be torn down and the data should persist inside the `data-volume` volume when the app service is brought back up.

#### app

This is the Django app and holds both the front-end and back-end components of it. The front-end is very simple, it's just an HTML template that displays a list of 3D prints. The back-end is also fairly straight forward as it asks for some details of your print and saves them to a Postgres database. 

#### database 

The database service is a container that handles all of the Postgres operations and sends the data to the `data-volume` Docker volume. This is all managed by Docker.

[insert diagram here]
