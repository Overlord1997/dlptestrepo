import json

def lambda_handler(event, context):
    # TODO implement jenkins DLP code master final
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
