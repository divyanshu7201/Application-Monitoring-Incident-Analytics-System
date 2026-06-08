import pandas as pd
import mysql.connector

class ErrorClassifier:
    def __init__(self, db_config):
        self.db_config = db_config

    def get_summary_statistics(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor(dictionary=True)
            
            query = """
            SELECT SeverityLevel, COUNT(*) as Count 
            FROM Logs 
            GROUP BY SeverityLevel
            ORDER BY Count DESC
            """
            
            cursor.execute(query)
            results = cursor.fetchall()
            
            print("--- Error Classification Summary ---")
            df = pd.DataFrame(results)
            if not df.empty:
                print(df.to_string(index=False))
            else:
                print("No data available.")
                
            return df
            
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'database': 'app_monitoring_db',
        'user': 'root',
        'password': '3344'
    }
    classifier = ErrorClassifier(db_config)
    classifier.get_summary_statistics()
