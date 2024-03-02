## SDE-Assessment
A Backend Application for Training Models.


## Features
- This application is build with ***Python-Flask***.
- ***Factory blueprint design pattern*** is used as backend framework architecture with MVC.
- To persist data, ***MySQL*** is used.
- ***Gunicorn*** is used to handle multiple requests. Default to 2 workers (can be increases depending on number of concurrent requests).
- ***Redis*** is used as a message broker for async tasks.
- ***Celery*** is used for the background and asynchrouns tasks.


## Project Structure
```bash
├─── app/
│    ├─── predict/
│    │    └─── __init__.py
│    │    └─── models.py
│    │    └─── views.py
│    │    └─── tasks.py
│    └─── utils/
│    │    └─── __init__.py
│    │    └─── parser.py
│    │    └─── responses.py
│    │    └─── schema.py
│    │    └─── training.py
│    ├─── __init__.py
│    ├─── celery_settings.py
│    ├─── database.py
│    ├─── exceptions.py
├─── docs/
│    ├─── PostmanCollection.json
│    │    └─── README.md
├─── .env
├─── config.py
├─── docker-compose.yaml
├─── Dockerfile
├─── Dockerfile.mysql
├─── gunicorn.conf.py
├─── requirements.txt
├─── requirements-dev.txt
├─── run.py
├─── schema.sql
├─── teardown.sh
├─── README.md

```
- `app/` folder contains all the application assets and resources.
- `config.py` is the settings file used to configure application properties.
- `run.py` is the starting point of the application.
- `requirements` files is used to list dependencies.
- `schema.sql` contains initial schema for the application.
- `Dockerfile` is used to build image for this application.
- `Dockerfile.mysql` is used to build image for sql server.
- `docker-compose.yaml` is used to build multiple images in a separate network.
- `gunicorn.conf.py` is the configurations file for the production flask app.
- `teardown.sh` is a bash script used to remove artifacts build during the process.


## Prerequisites
Make sure you have the following installed:
- Python 3.10 or higher
- Docker
- Git


## Docker/Production Setup
Follow the steps below to start the containerized application:
1. Upzip & navigate to the directory.
    ```console
    unzip sde-assessment.zip -d sde-assessment
    cd sde-assessment
    ```

2. Build the docker-compose file
    ```console
    docker-compose -f "./docker-compose.yaml" build
    ```

3. Start the docker-compose file
    ```console
    docker-compose -f "./docker-compose.yaml" up -d
    ```

4. Wait for few seconds (5 to 8 seconds) till mysql server gets started.

5. Start making request in the Postman Collection. Follow the [docs](docs/README.md) to get started with Postman Collection and documentation of endpoints.

6. Teardown process/artifacts. This will remove all the containers, volumes and images.
    ```console
    chmod u+x ./teardown.sh
    ./teardown.sh
    ```

## Local/Development Setup
Follow the steps below to start the application in development environment:
1. Upzip & navigate to the directory.
    ```console
    unzip sde-assessment.zip -d sde-assessment
    cd sde-assessment
    ```

2. Create a virtual environment
    ```console
    py -m virtualenv venv
    ```

3. Activate the virtual environment - May vary depending on the OS.
    ```console
    . .\venv\Scripts\activate
    ```

4. Install Dependencies
    ```console
    pip install -r requirements-dev.txt
    ```

5. Follow setups to setup database locally.
    1. Comment `flask` and `celery` services in `docker-compose.yaml` file.
    2. Run docker compose file `docker-compose up -d`

6. Start the flask application:
    ```console
    flask run -p 8080
    ```

7. Start the celery service in a separte terminal:
    ```console
    watchfiles --filter python 'celery -A run.celery worker --loglevel=info --pool=solo'
    ```

8. Start making request in the Postman Collection. Follow the [docs](docs/README.md) to get started with Postman Collection and documentation of endpoints.