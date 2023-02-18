# Week 0 — Billing and Architecture

## Install and Verify AWS CLI

I was able to use Gitpod to install aws-cli with instructions from the official AWS CLI Documentation.

`curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"`
`unzip awscliv2.zip`
`sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin`

Then I ran the following command to verify my installation
`aws --version`

## Create Budget with AWS CLI
I then created a budget using the command line (The account ID was gotten from aws sts get-caller-identity)
`aws budgets create-budget \`
`    --account-id $ACCOUNT_ID \`
`    --budget file://aws/json/budget.json \`
`    --notifications-with-subscribers file://aws/json/budget-notifications-with-subscribers.json`

## Create SNS with AWS CLI

I proceeded to create an SNS topic using:
`aws sns create-topic --name billing-alarm`

And ran the following command using the output from the previous command

`aws sns subscribe \`
`    --topic-arn="arn:aws:sns:us-east-1:898854645822:billing-alarm" \`
`    --protocol=email \`
`    --notification-endpoint=stephencharles02@gmail.com`


## Create Alarm with AWS CLI

Using the alarm-config file, I created an alarm on cloudwatch using:

`aws cloudwatch put-metric-alarm --cli-input-json file://aws/json/alarm-config.json`


## Logical Diagram
![Diagram of Logical Diagram](~/_docs/assets/logical-diagram.png)