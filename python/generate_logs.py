import csv
import random
import os
from datetime import datetime, timedelta

def generate_sample_logs(filename, num_records=15000):
    # Ensure directory exists
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    applications = ['PaymentGateway', 'AuthService', 'UserDashboard', 'OrderProcessing', 'InventoryManager']
    error_types = ['ConnectionTimeout', 'AuthenticationFailure', 'NullPointerException', 'OutOfMemoryError', 'DatabaseDeadlock']
    severities = ['Critical', 'High', 'Medium', 'Low']
    
    start_date = datetime.now() - timedelta(days=30)
    
    messages = {
        'ConnectionTimeout': 'Failed to connect to the upstream service within the allowed time.',
        'AuthenticationFailure': 'Invalid credentials provided for user login.',
        'NullPointerException': 'Attempted to access a null object reference.',
        'OutOfMemoryError': 'Java heap space out of memory.',
        'DatabaseDeadlock': 'Deadlock found when trying to get lock; try restarting transaction.'
    }

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'ApplicationName', 'ErrorType', 'ErrorMessage', 'SeverityLevel'])
        
        for _ in range(num_records):
            # Randomize timestamp over the last 30 days
            random_seconds = random.randint(0, 30 * 24 * 60 * 60)
            timestamp = start_date + timedelta(seconds=random_seconds)
            timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')
            
            app = random.choice(applications)
            error_type = random.choice(error_types)
            error_msg = messages[error_type]
            
            # Bias severity based on error type for realism
            if error_type in ['OutOfMemoryError', 'DatabaseDeadlock']:
                severity = random.choices(['Critical', 'High'], weights=[0.7, 0.3])[0]
            elif error_type == 'ConnectionTimeout':
                severity = random.choices(['High', 'Medium'], weights=[0.6, 0.4])[0]
            else:
                severity = random.choice(severities)
                
            writer.writerow([timestamp_str, app, error_type, error_msg, severity])

if __name__ == "__main__":
    # When running from the python directory or project root, ensure path is correct
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, '..', 'logs', 'sample_logs.csv')
    generate_sample_logs(output_path, 15500)
    print(f"Generated 15,500 sample logs at {output_path}")
