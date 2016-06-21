import json

def get_aws_credentials():
    credentials = None

    with open('config/defaults.json') as data:
        credentials = json.load(data)
    
    if 'Credentialss' in credentials:
        return credentials['Credentialss']
    else:
        raise Exception('There is no credentials in config/defaults.json file')