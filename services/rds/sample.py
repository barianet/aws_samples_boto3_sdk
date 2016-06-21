'''
====================
Boto 3 - RDS Example
====================
This application implements the RDS service that lets you gets
information from Amazon RDS. See the README for more details.
'''
import boto3
import json

config = json.loads(open('config/defaults.json').read())
credentials = config['credentials']

AWS_ACCESS_KEY_ID = credentials['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = credentials['aws_secret_access_key']
REGION_NAME = 'us-west-1'

rds = boto3.client('rds',
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                    region_name=REGION_NAME)

# print rds.describe_account_attributes()
# print rds.describe_db_instances()