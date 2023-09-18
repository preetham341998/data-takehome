# Import necessary functions from other modules
from sqs import receive_messages
from data_Processing import process_data
from database import write_to_postgres

def main():
    # Receive messages from SQS
    messages = receive_messages()
    
    for message in messages:
        # Process JSON data
        processed_data = process_data(message)
        
        #  Write to PostgreSQL
        write_to_postgres(processed_data)

if __name__ == "__main__":
    main()


