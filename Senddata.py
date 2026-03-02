import boto3
import random
import time
from datetime import datetime

alias = '/factory/Motor1/Speed'

client = boto3.client('iotsitewise', region_name='us-east-1')  

while True:
    speed = round(random.uniform(100, 1000), 2)
    epoch = int(time.time())
    readable_time = datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')

    payload = {
        "entries": [
            {
                "entryId": str(epoch),
                "propertyAlias": alias,
                "propertyValues": [
                    {
                        "value": {
                            "doubleValue": speed
                        },
                        "timestamp": {
                            "timeInSeconds": epoch
                        },
                        "quality": "GOOD"
                    }
                ]
            }
        ]
    }

    try:
        response = client.batch_put_asset_property_value(
            entries=payload['entries']
        )
        print(f"Sent Speed: {speed} | Epoch: {epoch} | Time: {readable_time}")
    except Exception as e:
        print("Error:", e)

    time.sleep(1)
