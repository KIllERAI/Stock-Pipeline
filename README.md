# NSE Stock Trade Streaming Pipeline
Real-time stock trade analytics pipeline on AWS — NSE ticker event producer, Kinesis ingestion, Lambda anomaly detection, S3/Redshift storage, QuickSight dashboard.


# Architecture
Producer → Kinesis Data Streams → Lambda (anomaly detection) → Kinesis Firehose → S3 (raw zone) → Glue ETL → S3 (curated zone) → Redshift → QuickSight

# Services Used
Python — trade event producer simulating NSE tickers
AWS Kinesis Data Streams — real-time event ingestion
AWS Lambda — anomaly detection (volume spikes >50,000)
AWS Kinesis Firehose — buffered delivery to S3 (date partitioned)
AWS S3 — raw and curated data lake zones
AWS Glue — PySpark ETL job adding trade_value metric
AWS Redshift — analytical data warehouse
AWS QuickSight — live trading dashboard
How to Run
Install dependencies: pip install boto3
Configure AWS credentials: aws configure
Run producer: python "generate stock data.py"
Monitor anomalies in CloudWatch logs
Run Glue ETL job to process raw data
Load into Redshift via COPY command
View dashboard in QuickSight
## Dashboard
[View QuickSight Dashboard](ss/Sheet_3_2026-06-05T09_05_13.pdf)
