CREATE TABLE IF NOT EXISTS patients (
    patient_id VARCHAR(50) PRIMARY KEY,
    full_name VARCHAR(150),
    date_of_birth DATE,
    gender VARCHAR(20),
    phone VARCHAR(20),
    insurance_id VARCHAR(50),
    admission_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS data_quality_issues (
    id BIGSERIAL PRIMARY KEY,
    patient_id VARCHAR(50),
    issue_type VARCHAR(80) NOT NULL,
    issue_details TEXT,
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pipeline_runs (
    id BIGSERIAL PRIMARY KEY,
    pipeline_name VARCHAR(120) NOT NULL,
    status VARCHAR(30) NOT NULL,
    records_processed INT DEFAULT 0,
    records_failed INT DEFAULT 0,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP
);
