'''
====================
Boto 3 - IAM Example
====================
This application implements the VPC service that lets you gets
information from Amazon VPC. See the README for more details.
'''
import boto3
import json

config = json.loads(open('config/defaults.json').read())
credentials = config['credentials']

AWS_ACCESS_KEY_ID = credentials['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = credentials['aws_secret_access_key']
REGION_NAME = 'us-west-1'

iam = boto3.client('iam',
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                    region_name=REGION_NAME)

# Filtering VPCs by tags:
filters = [{'Name':'tag:Name', 'Values':['webapp01']}]

webapp01 = list(ec2.vpcs.filter(Filters=filters))[0]
webapp01.vpc_id