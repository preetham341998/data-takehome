# Import necessary functions from other modules
from sqs import receive_messages
from data_Processing import process_data
from database import write_to_postgres

def main():
    # Step 1: Receive messages from SQS
    messages = receive_messages()
    
    for message in messages:
        # Step 2: Process JSON data
        processed_data = process_data(message)
        
        # Step 3: Write to PostgreSQL
        write_to_postgres(processed_data)

if __name__ == "__main__":
    main()


