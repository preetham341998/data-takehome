import boto3

def receive_messages():
    # Configure the SQS client
    sqs = boto3.client(
        'sqs',
        endpoint_url='http://localhost:4566',  
        region_name='us-east-1', 
        aws_access_key_id='placeholder',  
        aws_secret_access_key='placeholder', 
    )

    
    queue_url = 'http://localhost:4566/000000000000/login-queue'

    
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'All'
        ],
        MessageAttributeNames=[
            'All'
        ],
        MaxNumberOfMessages=10
    )

    # Extracting messages from response
    messages = response.get('Messages', [])
    return messages
