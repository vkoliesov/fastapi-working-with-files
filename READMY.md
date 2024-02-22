# Working with Read data from file and write these to DB via FastAPI

## To start project locally (via 🐋[Docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/)):

Into the project directory should create `.env` file and create values for database:`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT` and `POSTGRES_DB`


`docker compose up --build -d` (for the first run)
`docker compose up -d` (for subsequent runs)

Go to `http://localhost:8000/docs` to view Swagger API documentation


You can `/upload/` your files to your Google Drive,
`/download/` files from the Google Drive
`/create_folder/` to create folder on the Google Drive
`/delete/` to delete some file by name from The Google Drive
`/move/` to move some file from one place to another
