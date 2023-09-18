import boto3

def receive_messages():
    # Configure SQS client
    sqs = boto3.client(
        'sqs',
        endpoint_url='http://localhost:4566',  # Localstack SQS endpoint
        region_name='us-east-1',  # Use any region name
        aws_access_key_id='placeholder',  # Placeholder values
        aws_secret_access_key='placeholder',  # Placeholder values
    )

    # Replace 'queue_url' with the actual URL of your SQS Queue
    queue_url = 'http://localhost:4566/000000000000/login-queue'

    # Receive messages from the queue
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

    # Extract messages from response
    messages = response.get('Messages', [])
    return messages
