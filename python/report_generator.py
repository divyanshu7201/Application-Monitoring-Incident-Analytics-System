import pandas as pd
import mysql.connector
import os
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

class ReportGenerator:
    def __init__(self, db_config):
        self.db_config = db_config

    def generate_excel_report(self, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        try:
            conn = mysql.connector.connect(**self.db_config)
            
            # Fetch various datasets
            df_total_logs = pd.read_sql("SELECT COUNT(*) as TotalLogs FROM Logs", conn)
            df_severity = pd.read_sql("SELECT SeverityLevel, COUNT(*) as Count FROM Logs GROUP BY SeverityLevel ORDER BY Count DESC", conn)
            df_incidents = pd.read_sql("SELECT Status, COUNT(*) as Count FROM Incidents GROUP BY Status", conn)
            df_top_errors = pd.read_sql("SELECT ErrorType, COUNT(*) as Count FROM Logs GROUP BY ErrorType ORDER BY Count DESC LIMIT 10", conn)
            
            # Write to Excel
            with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                df_total_logs.to_excel(writer, sheet_name='Summary', index=False, startrow=0)
                df_severity.to_excel(writer, sheet_name='Summary', index=False, startrow=4)
                df_incidents.to_excel(writer, sheet_name='Summary', index=False, startrow=10)
                
                df_top_errors.to_excel(writer, sheet_name='Top Errors', index=False)
                
            print(f"Report successfully generated at {output_path}")
            
        except Exception as e:
            print(f"Failed to generate report: {e}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()

if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'database': 'app_monitoring_db',
        'user': 'root',
        'password': '3344'
    }
    generator = ReportGenerator(db_config)
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    report_path = os.path.join(script_dir, '..', 'reports', 'incident_report.xlsx')
    generator.generate_excel_report(report_path)
