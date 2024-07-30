
import json
from datetime import datetime, timedelta
import boto3

dynamodb = boto3.client('dynamodb', region_name='us-east-1')

def convert_and_schedule_event(date_str, time_str, rule_name, topic_arn, message, subject=None):
    # Parse the date and time
    event_datetime = datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M:%S")
    
    # Convert to UTC if it's not already
    # Uncomment and modify the next line if your input is not in UTC
    # event_datetime = event_datetime.replace(tzinfo=timezone.utc)
    
    # Create the cron expression
    cron_expression = f"cron({event_datetime.minute} {event_datetime.hour} {event_datetime.day} {event_datetime.month} ? {event_datetime.year})"
    
    # Create an EventBridge client
    events = boto3.client('events')

    # Create the rule
    rule_response = events.put_rule(
        Name=rule_name,
        ScheduleExpression=cron_expression,
        State='ENABLED'
    )
    
    # Prepare the input for the SNS message
    sns_params = {
        'TopicArn': topic_arn,
        'Message': message
    }
    
    if subject:
        sns_params['Subject'] = subject

    # Convert the SNS parameters to a JSON string
    input_json = json.dumps({'Sns': sns_params})

    target_response = events.put_targets(
        Rule=rule_name,
        Targets=[
            {
                'Id': '1',
                'Arn': topic_arn,
                'Input': input_json
            }
        ]
    )
    print(f"Created rule: {rule_name}")
    print(f"Rule ARN: {rule_response['RuleArn']}")
    print(f"Target SNS Topic: {topic_arn}")

    return rule_response['RuleArn']

def lambda_handler(event, context):
    print(event)
    agent = event['agent']
    actionGroup = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])
    sessionId = event['sessionId']
    hora = next((param['value'] for param in parameters if param['name'] == 'hora'), None)
    fecha = next((param['value'] for param in parameters if param['name'] == 'fecha'), None)
    descripcion = next((param['value'] for param in parameters if param['name'] == 'descripcion'), None)
    
    key = {'idsession': {'S': sessionId}} 

    response = dynamodb.get_item(TableName='users-registered-tfc-serverless', Key=key)
    
    mensaje = ''
    if 'Item' in response:
        topic_arn = response['Item']['snstopic']['S']
    else:
        topic_arn = None
    
    rule = convert_and_schedule_event(fecha, hora, descripcion.replace(" ", ""), topic_arn, descripcion, subject=None)

    # Execute your business logic here. For more information, refer to: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html
    responseBody =  {
        "TEXT": {
            "body": "Event Scheduled" 
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
