import boto3
import os
from botocore.exceptions import ClientError

#aws lambda function that sends an email using SES API
# input event contains from, to and body in plain text

def lambda_handler (event, context):


    #get the from, to and body from the event
    from_address = event['from']
    to_address = event['to']
    body = event['body']

    #get the SES client
    ses = boto3.client('ses')

    #send the email
    try:
        response = ses.send_email(
            Source=from_address,
            Destination={
                'ToAddresses': [
                    to_address,
                ]
            },
            Message={
                'Subject': {
                    'Data': 'Email from Lambda'
                },
                'Body': {
                    'Text': {
                        'Data': body
                    }
                }
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
    return {
        'statusCode': 200,
        'body': 'Email sent!'
    }