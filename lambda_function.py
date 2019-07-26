from __future__ import print_function
from fluent import sender
import os
import json
import boto3
import urllib
import gzip

print('Loading function')


def lambda_handler(event, context):
    # Set AWS Clients
    s3 = boto3.client('s3', region_name=os.environ['AWS_REGION'])

    # Set Fluentd client
    logger = sender.FluentSender('aws', host=os.environ['FLUENTD_HOST'], port=int(os.environ['FLUENTD_PORT']))

    # Load SNS message from event
    message = json.loads(event['Records'][0]['Sns']['Message'])

    # Retrieve bucket name and key from event
    bucket = message['s3Bucket']
    key = urllib.parse.unquote_plus(message['s3ObjectKey'][0])

    # Ignore Digest Events
    if 'Digest' in key:
        return "Cloudtrail Digest File - Not Processing"

    # Download gzip file and store events
    path = '/tmp/ctlog.gz'
    s3.download_file(bucket, key, path)
    gzfile = gzip.open(path, "r")
    events = json.loads(gzfile.readlines()[0])["Records"]
    for i in events:
        if 'Describe' not in i["eventName"]:
            i["@timestamp"] = i["eventTime"]
            i["eventSource"] = i["eventSource"].split(".")[0]
            i["dataSource"] = 'cloudtrail'
            data = json.dumps(i)
            print(data)
            logger.emit('cloudtrail', i)
            logger.close()
        else:
            print("CloudTrail Describe Event - Not Processing")