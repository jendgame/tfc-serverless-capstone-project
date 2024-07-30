
import json
import boto3

def lambda_handler(event, context):
    agent = event['agent']
    actionGroup = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])
    sessionId = event['sessionId']
    
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')  # Ajusta la región según sea necesario
    
    key = {'idsession': {'S': sessionId}} 

    response = dynamodb.get_item(TableName='users-registered-tfc-serverless', Key=key)
    
    mensaje = ''
    if 'Item' in response:
        print(response)
        mensaje = 'The user is registered. Welcome ' +  response['Item']['nombre']['S']
    else:
        mensaje = ' "El usuario no está registrado'

    # Execute your business logic here. For more information, refer to: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html
    responseBody =  {
        "TEXT": {
            "body": mensaje
        }
    }

    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': responseBody
        }

    }

    dummy_function_response = {'response': action_response, 'messageVersion': event['messageVersion']}
    print("Response: {}".format(dummy_function_response))

    return dummy_function_response
