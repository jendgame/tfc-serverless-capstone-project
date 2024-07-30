
import json
import boto3

def create_sns_topic_and_subscribe(topic_name, email):
    # Create an SNS client
    sns = boto3.client('sns')

    # Create the SNS topic
    response = sns.create_topic(Name=topic_name)
    topic_arn = response['TopicArn']
    print(f"Created SNS topic: {topic_arn}")

    # Subscribe email to the topic
    subscription = sns.subscribe(
        TopicArn=topic_arn,
        Protocol='email',
        Endpoint=email
    )
    print(f"Subscribed {email} to the topic")
    print(f"Subscription ARN: {subscription['SubscriptionArn']}")

    return topic_arn

def convert_to_dynamodb_format(data, session_id, sns_arn):
    dynamodb_item = {'idsession': {'S': session_id}, 'snstopic': {'S': sns_arn}}
    for entry in data:
        name = entry['name']
        type_ = entry['type']
        value = entry['value']

        if type_ == 'string':
            dynamodb_item[name] = {'S': value}
        elif type_ == 'number':
            dynamodb_item[name] = {'N': str(value)}
        # Añade más tipos según sea necesario (por ejemplo, 'B' para binarios, 'BOOL' para booleanos, etc.)

    return dynamodb_item

def lambda_handler(event, context):
    agent = event['agent']
    actionGroup = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])
    print(parameters)
    sessionId = event['sessionId']
    correo = next((param['value'] for param in parameters if param['name'] == 'correo'), None)
    sns_arn = create_sns_topic_and_subscribe(sessionId, correo)
    dynamodb_item = convert_to_dynamodb_format(parameters, sessionId, sns_arn) 

    dynamodb = boto3.client('dynamodb', region_name='us-east-1')

    
    
    mensaje = ''
    try:
        response = dynamodb.put_item(TableName='users-registered-tfc-serverless', Item=dynamodb_item)
        mensaje = 'Usuario registrado exitosamente'
    except Exception as e:
        print(e)
        mensaje = 'Hubo un error en el registro. Intenta de nuevo'
        

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
