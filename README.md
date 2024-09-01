## FastAPI app built according to the requirements.

To run for the first time:
### `docker-compose up --build`
For the consequential launch:
### `docker-compose up -d`
For tearing down containers and deleting any related volumes:
### `docker-compose down -v`

Starting containers may take some time (about 2 minutes) due to waiting for the MySQL database to fully initialize. The application presents books and their authors.
