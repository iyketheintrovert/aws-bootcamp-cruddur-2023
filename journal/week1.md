# Week 1 — App Containerization

## Create Docker File for Frontend & Backend

I created a Docker File for both the Frontend and the Backend folders, and used
```docker build``` to create docker images for both of them and then ```docker run``` to serve both.

### Set Env Vars for Frontend & Backend URL
```
export FRONTEND_URL=""
export BACKEND_URL=""
```

## Create Docker Compose File

I created a Docker Compose File, exposing the IPs for both the Frontend and the Backend and used ```docker compose up``` to serve the file.

The frontend was not served because node modules were not installed so i did the following:
```sd frontend-react-js```
```npm i```
```cd ..```
```docker compose up```


```docker build``` to create docker images for both of them and then ```docker run``` to serve both.



### Install AWS CLI

- We are going to install the AWS CLI when our Gitpod enviroment lanuches.
- We are are going to set AWS CLI to use partial autoprompt mode to make it easier to debug CLI commands.
- The bash commands we are using are the same as the [AWS CLI Install Instructions]https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html


Update our `.gitpod.yml` to include the following task.

```sh
tasks:
  - name: aws-cli
    env:
      AWS_CLI_AUTO_PROMPT: on-partial
    init: |
      cd /workspace
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
      cd $THEIA_WORKSPACE_ROOT
```

We'll also run these commands indivually to perform the install manually

### Create a new User and Generate AWS Credentials

- Go to (IAM Users Console](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/users) andrew create a new user
- `Enable console access` for the user
- Create a new `Admin` Group and apply `AdministratorAccess`
- Create the user and go find and click into the user
- Click on `Security Credentials` and `Create Access Key`
- Choose AWS CLI Access
- Download the CSV with the credentials

