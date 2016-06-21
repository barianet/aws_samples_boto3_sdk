'''
====================
Boto 3 - IAM Example
====================
This application implements the IAM service that lets you gets
information from Amazon IAM. See the README for more details.

A low-level client representing AWS Identity and Access Management (IAM).
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

print iam.list_policies()
print
print iam.list_roles()
print
print iam.list_users()
print

# iam.list_role_policies()
# iam.list_user_policies()