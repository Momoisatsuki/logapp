#!/usr/local/bin/python3
import boto3
import json
regions = ['us-east-1','us-west-2','ap-northeast-2','eu-central-1']
inventory = {}
count = int(0)

def get_cluster(region):
    client = boto3.client('ec2', region_name=region)
    reservations = client.describe_instances()['Reservations']
    for reservation in reservations:
        for instance in reservation['Instances']:
            if instance.__contains__('Tags'):
                for tag in instance['Tags']:
                    if tag['Key'] == "TNService":
                        if tag["Value"] == "Automotive":
                            for tag in instance['Tags']:
                                if tag['Key'] == "Name":
                                    if tag['Value'].split('-')[0].startswith('ec'):
                                        cluster = tag['Value'].split('-')[1]
                                        servername = tag['Value']
                                        if cluster in inventory:
                                            inventory[cluster].append(servername)
                                        else:
                                            inventory[cluster] = [servername]
                                        count += 1


if __name__ == "__main__":
    for region in regions:
        get_cluster(region)
print('total server count is: ' + count)
print(json.dumps(inventory))