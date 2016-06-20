'''
===================================
Boto 3 - CloudWatch Service Example
===================================
This application implements the CloudWatch service that lets you gets
information from Amazon Cloud Watch. See the README for more details.
'''
import boto3

'''
Define your AWS credentials:
'''
AWS_ACCESS_KEY_ID = '<YOUR ACCESS KEY ID>'
AWS_SECRET_ACCESS_KEY = '<YOUR SECRET ACCESS KEY>'

'''
Connection to AWS.
'''
client = boto3.client('cloudwatch',
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Main program:
if __name__ == '__main__':
    print_results()