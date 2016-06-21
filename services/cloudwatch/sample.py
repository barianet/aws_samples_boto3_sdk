'''
===================================
Boto 3 - CloudWatch Service Example
===================================
This application implements the CloudWatch service that lets you gets
information from Amazon Cloud Watch. See the README for more details.
'''
import boto3
import json

config = json.loads(open('config/defaults.json').read())
credentials = config['credentials']

AWS_ACCESS_KEY_ID = credentials['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = credentials['aws_secret_access_key']
REGION_NAME = 'us-west-1'

client = boto3.client('cloudwatch',
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                        region_name=REGION_NAME)

# def get_metric_stats():
#     response = client.get_metric_statistics(
#         Namespace='AWS/S3',
#         MetricName='BucketSizeBytes',
#         StartTime=datetime.utcnow() - timedelta(days=1),
#         EndTime=datetime.utcnow(),
#         Period=86400,
#         Statistics=['Sum'],
#         Unit='Bytes',
#         Dimensions=[{'Name':'BucketName', 'Value':'backup-bucket'}]
#     )
#     return response

# def get_list_metrics():
#     response = client.list_metrics(
#         Namespace='string',
#         MetricName='string',
#         Dimensions=[
#             {
#                 'Name': 'string',
#                 'Value': 'string'
#             },
#         ],
#         NextToken='string'
#     )
#     return response

# Main program:
if __name__ == '__main__':
    print client.list_metrics()
