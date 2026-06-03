import json
import base64

def lambda_handler(event,context):
    for record in event['Records']:
        payload = base64.b64decode(record['kinesis']['data'])
        trade = json.loads(payload)
        if trade['volume'] > 50000:
            print(f"High volume trade anomaly: {trade}")
        else:
             print(f"Normal trade: {trade}")

if __name__ == "__main__":
    test_event = {
        "Records": [
            {
                "kinesis": {
                    "data": base64.b64encode(json.dumps({
                        "ticker": "SBIN",
                        "price": 499.0,
                        "volume": 75000,
                        "timestamp": "2026-06-03T10:00:00",
                        "trade_type": "BUY"
                    }).encode()).decode()
                }
            }
        ]
    }
    lambda_handler(test_event, None)