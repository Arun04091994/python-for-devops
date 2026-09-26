boto3 first video

control+shift+p > devcontainer > aws cli > save the added file to install aws cli
control+shift+p > Codespaces: Rebuild Container

aws configure
pip install boto3 or pip3 install boto3

create test.py

import boto3
client = boto3.client('s3')

follow boto3 documentation and search for available services and choose the services

for create s3, to get s3 acl add request syntax code and put only required attributes as we are just testing it

note
botocore - exceptions --> this module will handle try and except

boto3 second video
lambda_handler is the function lambda by default first triggers it. you can change by changing configuration. this lambda_handler function should call other functions.o`
lambda functions will be mostly used to monitor cost optimization and security/compliance like to check if resources are built with unallowed sizes and storages.

create lambda function and check configuration in it
you can get environment variable option to declare variables
by default lambda will create a default role
function url can enable while during creation to allow url to accessible
lambda can be deployed in VPC

create ec2 and snapshot
create lambda function, attach ec2 describe, volume describe, snapshot describe and snapshot delete policy permissions to lambda role
create lambda
test the functionality
understand the program
