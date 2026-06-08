-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS app_monitoring_db;
USE app_monitoring_db;

-- Table for tracking Engineers
CREATE TABLE IF NOT EXISTS Engineers (
    EngineerID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Specialization VARCHAR(50)
);

-- Table for storing Logs
CREATE TABLE IF NOT EXISTS Logs (
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    Timestamp DATETIME NOT NULL,
    ApplicationName VARCHAR(100) NOT NULL,
    ErrorType VARCHAR(100) NOT NULL,
    ErrorMessage TEXT NOT NULL,
    SeverityLevel ENUM('Critical', 'High', 'Medium', 'Low') NOT NULL,
    ProcessedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing Incidents
CREATE TABLE IF NOT EXISTS Incidents (
    IncidentID INT AUTO_INCREMENT PRIMARY KEY,
    LogID INT NOT NULL,
    AssignedEngineerID INT,
    Status ENUM('Open', 'In Progress', 'Resolved') DEFAULT 'Open',
    ResolutionNotes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (LogID) REFERENCES Logs(LogID),
    FOREIGN KEY (AssignedEngineerID) REFERENCES Engineers(EngineerID)
);

-- Table for storing Resolution History
CREATE TABLE IF NOT EXISTS ResolutionHistory (
    HistoryID INT AUTO_INCREMENT PRIMARY KEY,
    IncidentID INT NOT NULL,
    StatusChange VARCHAR(50) NOT NULL,
    Notes TEXT,
    ChangedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (IncidentID) REFERENCES Incidents(IncidentID)
);

-- Insert sample engineers
INSERT INTO Engineers (Name, Email, Specialization) VALUES
('Alice Smith', 'alice@support.com', 'Database'),
('Bob Johnson', 'bob@support.com', 'Backend'),
('Charlie Davis', 'charlie@support.com', 'Frontend'),
('Diana Prince', 'diana@support.com', 'Network');
