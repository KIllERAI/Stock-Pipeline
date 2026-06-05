
# NSE Stock Trade Streaming Pipeline

Real-time stock trade analytics pipeline built on AWS using NSE equity tickers.

## Architecture

Producer → Kinesis Data Streams → Lambda (anomaly detection) → Kinesis Firehose → S3 (raw zone) → Glue ETL → S3 (curated zone) → Redshift → QuickSight

## Services Used

- **Python** — trade event producer simulating NSE tickers
- **AWS Kinesis Data Streams** — real-time event ingestion
- **AWS Lambda** — anomaly detection (volume spikes >50,000)
- **AWS Kinesis Firehose** — buffered delivery to S3 (date partitioned)
- **AWS S3** — raw and curated data lake zones
- **AWS Glue** — PySpark ETL job adding trade_value metric
- **AWS Redshift** — analytical data warehouse
- **AWS QuickSight** — live trading dashboard

## How to Run

1. Install dependencies: `pip install boto3`
2. Configure AWS credentials: `aws configure`
3. Run producer: `python "generate stock data.py"`
4. Monitor anomalies in CloudWatch logs
5. Run Glue ETL job to process raw data
6. Load into Redshift via COPY command
7. View dashboard in QuickSight
