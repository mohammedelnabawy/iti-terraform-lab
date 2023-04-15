import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("ses")
    subject = "test subject from lambda"
    body = "your aws resources is changed"
    message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
    response = client.send_email(Source = "Your mail address in SES",
               Destination = {"ToAddresses": ["Your mail address in SES"]}, Message = message)
    return response
