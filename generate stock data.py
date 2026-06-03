import json
import random
from datetime import datetime
import time
import boto3

kinesis = boto3.client('kinesis', region_name='us-east-1')
tickers = ['INFY', 'HDFCBANK', 'RELIANCE', 'TCS', 'ICICIBANK', 'HINDUNILVR', 'KOTAKBANK', 'SBIN', 'ITC', 'LT']
base_price = {
    'INFY': 1500,
    'HDFCBANK': 1200,
    'RELIANCE': 2000,
    'TCS': 3000,
    'ICICIBANK': 800,
    'HINDUNILVR': 2500,
    'KOTAKBANK': 1800,
    'SBIN': 500,
    'ITC': 1000,
    'LT': 2200
}
          
def generate_stock_data():
        ticker = random.choice(tickers)
        price = base_price[ticker] + random.uniform(-50, 50)
        if random.random() < 0.05:
            volume = random.randint(50000,200000)
        else:
            volume = random.randint(1000, 10000)
        timestamp = datetime.now().isoformat()
        trade_type = random.choice(['BUY','SELL'])
        return({
            'ticker': ticker,
            'price': round(price, 2),
            'volume': volume,
            'timestamp': timestamp,
            'trade_type': trade_type
            })

while True:
    trade = generate_stock_data()
    kinesis.put_record(
        StreamName='stock-trades-stream',
        Data=json.dumps(trade),
        PartitionKey=trade['ticker']
    )
    print(f"Sent: {json.dumps(trade)}")
    time.sleep(1)
    # time.sleep(1) 
# print(json.dumps(generate_stock_data()))
