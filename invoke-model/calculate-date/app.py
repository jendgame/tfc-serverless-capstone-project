
import json
from datetime import datetime


def lambda_handler(event, context):
    agent = event['agent']
    actionGroup = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])


    # Obtén la fecha y hora actual en la zona horaria de Colombia
    colombia_time = datetime.now()

    # Execute your business logic here. For more information, refer to: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html
    responseBody =  {
        "TEXT": {
            "body": "la fecha actual es " + colombia_time.strftime("%d/%m/%Y")
        }
    }

    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': responseBody
        }

    }

    dummy_function_response = {'response': action_response, 'messageVersion': "la fecha actual es" + colombia_time.strftime("%d/%m/%Y %H:%M:%S")}
    print("Response: {}".format(dummy_function_response))

    return dummy_function_response
