import json
import boto3
import base64
import urllib.parse
import re
from datetime import datetime

from twilio.twiml.messaging_response import MessagingResponse

bedrock_runtime = boto3.client(
    service_name='bedrock-agent-runtime',
    region_name='us-east-1'  # e.g., 'us-west-2'
)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('conversation-history')



def lambda_handler(event, context):
    
    print(event)
    body = event['body']
    
        
    
    # Analizar la query string
    parsed_query = urllib.parse.parse_qs(body)
    
    # Obtener el valor del parámetro 'From'
    from_value = parsed_query.get('From', [None])[0]
    from_number = re.sub(r'\D', '', from_value)
    message_body = parsed_query.get('Body', [None])[0]

    agent_id = "DL1XICZKBU"
    agent_alias_id = "0P2V9VSTKR"
    session_id = from_number
    current_datetime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    
    table.put_item(Item={
        'session_id': session_id,
        'date': current_datetime,
        'role': 'person',
        'message': message_body
    })

    

    response = bedrock_runtime.invoke_agent(
        agentId=agent_id,
        agentAliasId=agent_alias_id,
        sessionId=session_id, 
        inputText=message_body)
        
    
    completion = ""
    
    for event in response.get("completion"):
        chunk = event["chunk"]
        completion = completion + chunk["bytes"].decode()
    
    resp = MessagingResponse()
    resp.message(completion)
    
    current_datetime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    
    table.put_item(Item={
        'session_id': session_id,
        'date': current_datetime,
        'role': 'agent',
        'message': completion
    })
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/xml'
        },
        'body': str(resp)
    }
