#!/usr/local/bin/python3
import boto3
import json

inventory = {}

def get_cluster(region):
    client = boto3.client('ec2', region_name="us-east-1")
    reservations = client.describe_instances()['Reservations']
    for reservation in reservations:
        for instance in reservation['Instances']:
            for tag in instance['Tags']:
                if tag['Key'] == "TNService":
                    if tag["Value"] == "Automotive":
                        for tag in instance['Tags']:
                            if tag['Key'] == "Name":
                                cluster = tag['Value'].split('-')[1]
                                servername = tag['Value']
                                if cluster in inventory:
                                    inventory[cluster].append(servername)
                                else:
                                    inventory[cluster] = [servername]


if __name__ == "__main__":
    for region in ['us-east-1','us-west-2','ap-northeast-2','eu-central-1']:
        get_cluster(region)

print(inventory)