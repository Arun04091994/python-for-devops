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
create lambda function and check configuration in it

create ec2 and snapshot
create lambda function, attach ec2 describe, volume describe, snapshot describe and snapshot delete policy permissions to lambda role
create lambda
test the functionality
understand the program
