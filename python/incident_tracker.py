import mysql.connector

class IncidentTracker:
    def __init__(self, db_config):
        self.db_config = db_config

    def create_incidents_from_critical_logs(self):
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor(dictionary=True)
            
            # Find Critical logs that don't have an incident yet
            query = """
            SELECT l.LogID
            FROM Logs l
            LEFT JOIN Incidents i ON l.LogID = i.LogID
            WHERE l.SeverityLevel IN ('Critical', 'High') AND i.IncidentID IS NULL
            """
            cursor.execute(query)
            critical_logs = cursor.fetchall()
            
            if not critical_logs:
                print("No new critical logs to create incidents for.")
                return 0
                
            # Assign incidents in round-robin fashion to engineers
            cursor.execute("SELECT EngineerID FROM Engineers")
            engineers = [row['EngineerID'] for row in cursor.fetchall()]
            
            if not engineers:
                print("No engineers found in the database. Cannot assign incidents.")
                return 0
                
            incidents_created = 0
            for i, log in enumerate(critical_logs):
                engineer_id = engineers[i % len(engineers)]
                
                insert_query = """
                INSERT INTO Incidents (LogID, AssignedEngineerID, Status)
                VALUES (%s, %s, 'Open')
                """
                cursor.execute(insert_query, (log['LogID'], engineer_id))
                
                # Log to resolution history
                incident_id = cursor.lastrowid
                history_query = """
                INSERT INTO ResolutionHistory (IncidentID, StatusChange, Notes)
                VALUES (%s, %s, %s)
                """
                cursor.execute(history_query, (incident_id, 'Open', 'Incident automatically created from critical log.'))
                incidents_created += 1
                
            conn.commit()
            print(f"Created {incidents_created} new incidents.")
            return incidents_created
            
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return 0
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
    tracker = IncidentTracker(db_config)
    tracker.create_incidents_from_critical_logs()
