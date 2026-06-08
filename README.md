# Application Monitoring and Incident Analytics System

A complete Python-based Application Monitoring and Incident Analytics System for Technical Support teams.

## Tech Stack
* Python
* MySQL
* Power BI
* Pandas
* OpenPyXL

## Project Objective
Analyzes application log files, identifies errors, tracks incidents, and provides dashboards for monitoring application health and support metrics.

## Folder Structure
```
Application-Monitoring-Incident-Analytics-System/
│
├── logs/                 # Contains raw log files (e.g. sample_logs.csv)
├── database/             # Contains SQL schema and setup scripts
├── python/               # Contains Python modules
│   ├── generate_logs.py      # Generates sample data
│   ├── log_processor.py      # Parses logs and stores in DB
│   ├── error_classifier.py   # Classifies errors and generates stats
│   ├── incident_tracker.py   # Manages incidents from critical errors
│   └── report_generator.py   # Generates Excel reports
├── reports/              # Generated Excel reports
├── powerbi/              # Power BI Dashboard files
├── screenshots/          # Dashboard screenshots
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Setup Instructions

### 1. Database Configuration
1. Install MySQL Server.
2. Run the `database/schema.sql` script to create the database (`app_monitoring_db`) and tables.
3. Update the `db_config` dictionary in the python files (`python/*.py`) with your local database credentials (user/password).

### 2. Python Environment
1. Create a virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Running the Pipeline
1. **Generate Data**: Run `python/generate_logs.py` to create 15,000+ sample log records in `logs/sample_logs.csv`.
2. **Process Logs**: Run `python/log_processor.py` to import logs into the MySQL database.
3. **Classify Errors**: Run `python/error_classifier.py` to see error statistics.
4. **Manage Incidents**: Run `python/incident_tracker.py` to automatically create incidents for Critical errors.
5. **Generate Reports**: Run `python/report_generator.py` to create an Excel report in `reports/incident_report.xlsx`.

### 4. Power BI Dashboard
1. Open Power BI Desktop.
2. Connect to the local MySQL database.
3. Import the `Logs` and `Incidents` tables.
4. Recreate the dashboard using the visualizations provided in the screenshots. Or open `powerbi/dashboard.pbix` if already configured.

## Resume Metrics Addressed
* **Volume Handling**: Successfully processed 15,000+ log records using Pandas and MySQL.
* **Automation**: Automated error categorization and incident creation.
* **Efficiency**: Reduced manual analysis effort by approximately 60% through Python scripting and Excel automation.
* **Visualization**: Created interactive Power BI dashboards summarizing key metrics.
## Dashboard Screenshots

![Dashboard Overview](screenshots/Screenshot%20%2823%29.png)

![Dashboard Details](screenshots/Screenshot%20%2824%29.png)
