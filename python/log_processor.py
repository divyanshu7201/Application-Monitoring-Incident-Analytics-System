import pandas as pd
import mysql.connector
from mysql.connector import Error

class LogProcessor:
    def __init__(self, db_config):
        self.db_config = db_config

    def connect(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            return conn
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    def process_logs(self, file_path):
        print(f"Reading logs from {file_path}...")
        df = pd.read_csv(file_path)
        
        # Basic validation
        required_columns = ['Timestamp', 'ApplicationName', 'ErrorType', 'ErrorMessage', 'SeverityLevel']
        if not all(col in df.columns for col in required_columns):
            raise ValueError(f"Missing required columns. Expected: {required_columns}")
            
        print(f"Processing {len(df)} log records...")
        
        conn = self.connect()
        if not conn:
            return
            
        cursor = conn.cursor()
        
        insert_query = """
        INSERT INTO Logs (Timestamp, ApplicationName, ErrorType, ErrorMessage, SeverityLevel)
        VALUES (%s, %s, %s, %s, %s)
        """
        
        # Convert dataframe to list of tuples
        records = df[required_columns].values.tolist()
        
        try:
            cursor.executemany(insert_query, records)
            conn.commit()
            print(f"Successfully inserted {cursor.rowcount} records into Logs table.")
        except Error as e:
            print(f"Failed to insert records: {e}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    # Example usage (update with actual credentials when running)
    db_config = {
        'host': 'localhost',
        'database': 'app_monitoring_db',
        'user': 'root',
        'password': '3344'
    }
    processor = LogProcessor(db_config)
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(script_dir, '..', 'logs', 'sample_logs.csv')
    processor.process_logs(log_file_path)
