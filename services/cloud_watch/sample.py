'''
===================================
Boto 3 - CloudWatch Service Example
===================================
This application implements the CloudWatch service that lets you gets
information from Amazon Cloud Watch. See the README for more details.
'''
import boto3

AWS_ACCESS_KEY_ID = '<YOUR ACCESS KEY ID>'
AWS_SECRET_ACCESS_KEY = '<YOUR SECRET ACCESS KEY>'

# client = boto3.client('cloudfront')
client = boto3.client('cloudfront',
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

distributions = client.list_distributions()
streaming_distributions = client.list_streaming_distributions()
# origin_access_identities = client.list_cloud_front_origin_access_identities()
# distributions_by_web_acl_id = client.list_distributions_by_web_acl_id(WebACLId='')
# invalidations = client.list_invalidations(DistributionId='')

def get_default_cache_behavior(behavior=None):
    if behavior is None:
        print 'None'
        return None
    print 'TrustedSigners: {}'.format(behavior['TrustedSigners'])
    print 'TargetOriginId: {}'.format(behavior['TargetOriginId'])
    print 'ViewerProtocolPolicy: {}'.format(behavior['ViewerProtocolPolicy'])
    print 'ForwardedValues: {}'.format(behavior['ForwardedValues'])
    print 'MaxTTL: {}'.format(behavior['MaxTTL'])
    print 'PathPattern: {}'.format('Default (*)')
    print 'SmoothStreaming: {}'.format(behavior['SmoothStreaming'])
    print 'DefaultTTL: {}'.format(behavior['DefaultTTL'])
    print 'AllowedMethods: {}'.format(behavior['AllowedMethods'])
    print 'MinTTL: {}'.format(behavior['MinTTL'])
    print 'Compress: {}'.format(behavior['Compress'])

def get_behaviors(behaviors=None):
    if behaviors is None:
        print 'None'
        return None
    for behavior in behaviors['Items']:
        print 'TrustedSigners: {}'.format(behavior['TrustedSigners'])
        print 'TargetOriginId: {}'.format(behavior['TargetOriginId'])
        print 'ViewerProtocolPolicy: {}'.format(behavior['ViewerProtocolPolicy'])
        print 'ForwardedValues: {}'.format(behavior['ForwardedValues'])
        print 'MaxTTL: {}'.format(behavior['MaxTTL'])
        print 'PathPattern: {}'.format(behavior['PathPattern'])
        print 'SmoothStreaming: {}'.format(behavior['SmoothStreaming'])
        print 'DefaultTTL: {}'.format(behavior['DefaultTTL'])
        print 'AllowedMethods: {}'.format(behavior['AllowedMethods'])
        print 'MinTTL: {}'.format(behavior['MinTTL'])
        print 'Compress: {}'.format(behavior['Compress'])

def get_restrictions(restrictions=None):
    if restrictions is None:
        print 'None'
        return None
    print 'GeoRestriction: {}'.format(restrictions['GeoRestriction'])
    print 'Type: {}'.format(restrictions['GeoRestriction']['RestrictionType'])
    print 'Status: {}'.format(restrictions['GeoRestriction']['Quantity'])

def get_error_pages(error_pages=None):
    if error_pages['Quantity'] <= 0:
        print 'None'
        return None
    for error_page in error_pages['Items']:
        print 'ErrorCode: {}'.format(error_page['ErrorCode'])
        print 'ResponsePagePath: {}'.format(error_page['ResponsePagePath'])
        print 'ResponseCode: {}'.format(error_page['ResponseCode'])
        print 'ErrorCachingMinTTL: {}'.format(error_page['ErrorCachingMinTTL'])

def get_origins(origins=None):
    if origins['Quantity'] <= 0:
        print 'None'
        return None
    for origin in origins['Items']:
        print 'OriginPath: {}'.format(origin['OriginPath'])
        print 'CustomHeaders: {}'.format(origin['CustomHeaders'])
        print 'Id: {}'.format(origin['Id'])
        print 'DomainName: {}'.format(origin['DomainName'])
        if origin.get('S3OriginConfig') is not None:
            print 'S3OriginConfig: {}'.format(origin['S3OriginConfig'])
        if origin.get('CustomOriginConfig') is not None:
            print 'CustomOriginConfig: {}'.format(origin['CustomOriginConfig'])

def get_list_distributions(distribution=None):
    # print '---------------------------------'
    # print distribution
    # print '---------------------------------'
    print 'Name: {}'.format(distribution['DomainName'])
    print 'Id: {}'.format(distribution['Id'])
    print 'Delivery Method: AAAA'
    print 'Comment: {}'.format(distribution['Comment'])
    print 'CNames: BBB'
    print 'Status: {}'.format(distribution['Status'])
    print 'State: {}'.format(distribution['Enabled'])
    print 'LastModifiedTime: {}'.format(distribution['LastModifiedTime'])
    print 'Price Class: {}'.format(distribution['PriceClass'])
    print 'ViewerCertificate: {}'.format(distribution['ViewerCertificate'])

def get_x(dist=None):
    if dist is None:
        return None
    print 'Dist ----- ', dist
    print


def p(behaviors, column):
    print '-----------------------'
    res = [(b['TargetOriginId'], b[column]) for b in behaviors]
    print res
    print '-----------------------'

def print_results():
    if distributions:
        for dist in distributions['DistributionList']['Items']:
            helper = Boto3Helper(distribution=dist)

            dist['behaviors'] = helper.get_behaviors()
            dist['restrictions'] = helper.get_restrictions()
            dist['error_pages'] = helper.get_custom_error_responses()
            dist['origins'] = helper.get_origins()
            dist['invalidations'] = client.list_invalidations(DistributionId=dist['Id'],)
            dist['delivery_method'] = 'Web'

        for dist in distributions['DistributionList']['Items']:
            invs = []
            if dist and 'invalidations' in dist:
                for inv in dist['invalidations']['InvalidationList'].get('Items', []):
                    inv = client.get_invalidation(DistributionId=dist['Id'], Id=inv['Id'])
                    invs.append(inv)
            dist['invalidation_details'] = invs

        # for distribution in distributions['DistributionList']['Items']:
        #     print '===================================================================='
        #     print 'CloudFront Distribution ID: {}'.format(distribution['Id'])
        #     print '===================================================================='
        
        for dist in streaming_distributions['StreamingDistributionList']['Items']:
            dist['rtmpdistribution'] = client.get_streaming_distribution(Id=dist['Id'])
            dist['delivery_method'] = 'RTMP'

        for dist in streaming_distributions['StreamingDistributionList']['Items']:
            print dist['rtmpdistribution']
            print dist['delivery_method']
            # p(distribution['behaviors'], 'TargetOriginId')
            # p(distribution['behaviors'], 'TrustedSigners')
            # p(distribution['behaviors'], 'ViewerProtocolPolicy')
            # p(distribution['behaviors'], 'ForwardedValues')
            # p(distribution['behaviors'], 'PathPattern')
            # p(distribution['behaviors'], 'MaxTTL')
            # p(distribution['behaviors'], 'MinTTL')
            # p(distribution['behaviors'], 'DefaultTTL')
            # p(distribution['behaviors'], 'AllowedMethods')
            # p(distribution['behaviors'], 'Compress')

            # get_x(distribution['behaviors'])
            # get_x(distribution['restrictions'])
            # get_x(distribution['error_pages'])
            # get_x(distribution['origins'])
            # get_x(distribution['invalidations'])
            # get_x(distribution['delivery_method'])

class Boto3Helper():
    def __init__(self, distribution=None, rtmpdistribution=None):
        self.dist = distribution
        self.rtmpdist = rtmpdistribution

    def get_behaviors(self):
        has_cache_behaviors = self.dist.has_key('CacheBehaviors')
        has_default_cache_behavior = self.dist.has_key('DefaultCacheBehavior')
        result = []

        if has_cache_behaviors:
            items = self.dist['CacheBehaviors'].get('Items')
            if items:
                result = items

        if has_default_cache_behavior:
            temp_behavior = self.dist['DefaultCacheBehavior']
            temp_behavior['PathPattern'] = 'Default (*)'
            result.append(temp_behavior)
        return result

    def get_restrictions(self):
        has_restrictions = self.dist.has_key('Restrictions')
        result = {}
        if has_restrictions:
            result = self.dist['Restrictions']
        return result

    def get_custom_error_responses(self):
        has_custom_error_responses = self.dist.has_key('CustomErrorResponses')
        result = {}
        if has_custom_error_responses:
            items = self.dist['CustomErrorResponses'].get('Items')
            if items:
                result = items
        return result

    def get_origins(self):
        has_origins = self.dist.has_key('Origins')
        result = {}
        if has_origins:
            items = self.dist['CustomErrorResponses'].get('Items')
            if items:
                result = items
        return result

# Main program:
if __name__ == '__main__':
    print_results()