**boto3 first video**

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

**boto3 second video**
lambda_handler is the function lambda by default first triggers it. you can change by changing configuration. this lambda_handler function should call other functions.
lambda functions will be mostly used to monitor cost optimization and security/compliance like to check if resources are built with unallowed sizes and storages.
create lambda function by enabling URL option, don't use VPC, use default role and check configuration in it.
you can get environment variable option to declare variables
by default lambda will create a default role
function url can enable while during creation to allow url to accessible
lambda can be deployed in VPC

**boto3 third video - cost optimization**
create ec2 and snapshot
create lambda function, increase timeout from 3 to 10 sec in lambda configuration tab-[
create snapshot describe, snapshot delete policy permissions to lambda role. add describe ec2 and describe volume permissions
test the functionality
snapshot should not be deleted when associated volume is in attached state
remove ec2, volume and test it again

**below is the program**

in boto3 documentation get the code for all ec2 instances8888888888888888888888888888888888888888888888

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get all EBS snapshots
    response = ec2.describe_snapshots(OwnerIds=['self'])

    # Get all active EC2 instance IDs
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instance_ids = set()

    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    # Iterate through each snapshot and delete if it's not attached to any volume or the volume is not attached to a running instance
    for snapshot in response['Snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

        if not volume_id:
            # Delete the snapshot if it's not attached to any volume
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
        else:
            # Check if the volume still exists
            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")
