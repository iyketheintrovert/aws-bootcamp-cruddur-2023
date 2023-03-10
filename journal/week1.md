# Week 1 — App Containerization

## Create Docker File for Frontend & Backend

I created a Docker File for both the Frontend and the Backend folders, and used
```docker build``` to create docker images for both of them and then ```docker run``` to serve both.

### Set Env Vars for Frontend & Backend URL
```
export FRONTEND_URL=""
export BACKEND_URL=""
```
```docker run --rm -p 4567:4567 -it -e FRONTEND_URL="*" -e BACKEND_URL="*" backend-flask```

## Create Docker Compose File

I created a Docker Compose File, exposing the IPs for both the Frontend and the Backend and used ```docker compose up``` to serve the file.

The frontend was not served because node modules were not installed so i did the following:
```sd frontend-react-js```
```npm i```
```cd ..```
```docker compose up```


## Update Notifications

Added code for installing clients for Dynamo DB and Postgres in my Docker File
Also install postgres when our Gitpod enviroment lanuches.


## Add Dynamo DB and Postgres

Added code for installing clients for Dynamo DB and Postgres in my Docker File
Also install postgres when our Gitpod enviroment lanuches.
