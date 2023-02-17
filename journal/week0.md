# Week 0 — Billing and Architecture

## Install and Verify AWS CLI

I was able to use Gitpod to install aws-cli with instructions from the official AWS CLI Documentation.

`curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"`
`unzip awscliv2.zip`
`sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin`

Then I ran the following command to verify my installation
`aws --version`