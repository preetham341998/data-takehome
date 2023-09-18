import json
import hashlib
import uuid

#  hash PII fields (device_id and ip)
def hash_pii_values(device_id, ip):
    hashed_device_id = hashlib.sha256(device_id.encode()).hexdigest()
    hashed_ip = hashlib.sha256(ip.encode()).hexdigest()
    return hashed_device_id, hashed_ip

def process_data(message):
    body = message['Body']
    try:
        data = json.loads(body)
        
        #Extract relevant fields from JSON
        user_id = data['user_id']
        device = data['device']
        ip = data['ip']
        locale = data['locale']
        app_version = data['app_version']
        create_date = data['create_date']

        

        device_type, masked_device_id = split_device_field(device)
        
        # Hash PII fields 'device_id' and 'ip'
        hashed_device_id, hashed_ip = hash_pii_values(device, ip)
        
        # Create a flattened data structure matching the table columns
        flattened_data = {
            'user_id': user_id,
            'device_type': device_type,
            'masked_device_id': hashed_device_id,  # Stores hashed device_id
            'masked_ip': hashed_ip,  # Stores hashed ip
            'locale': locale,
            'app_version': app_version,
            'create_date': create_date
        }
        
        # Process the data as needed
        processed_data = flattened_data
        
        return processed_data
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")


