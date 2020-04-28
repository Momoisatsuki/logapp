#!/usr/local/bin/python3
import boto3
import json

inventory = {}


client = boto3.client('ec2', region_name="us-east-1")
reservations = client.describe_instances()['Reservations']

#reservations[0]['Instances']['Tags']
for reservation in reservations:
    for instance in reservation['Instances']:
        for tag in instance['Tags']:
            if tag['Key'] == "TNService":
                if tag["Value"] == "Automotive":
                    for tag in instance['Tags']:
                        if tag['Key'] == "Name":
                            cluster = tag['Value'].split('-')[1]
                            servername = tag['Value']
                            #print(cluster)
                            #print(servername)
                            if servername in inventory:
                                inventory[cluster].append(servername)
                            else:
                                inventory[cluster] = [cluster]
print(inventory)