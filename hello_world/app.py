import json

# import requests


def lambda_handler(event, context):

    personId = event['queryStringParameters']['personId']

    return {
        "statusCode": 200,
        "body": json.dumps({
            "personId": personId + " from Lambda" ,
        }),
    }
