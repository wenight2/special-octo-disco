def handler(event, context):
    print(event)
    something = str(event["headers"])
    return {'body': something,
            'statusCode': 200
            }
