import json
from kafka import KafkaConsumer
from datetime import datetime
import boto3

TOPIC = "hackernews"
BUCKET_NAME = "kafka-s3-strem"   # <-- your bucket name

# Create S3 client (uses aws configure credentials)
s3 = boto3.client("s3")

# Create Kafka consumer
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="hackernews-s3-consumer-v1"
)

print("Kafka consumer started... waiting for messages")

for message in consumer:
    data = message.value
    print("Received message from Kafka")

    timestamp = datetime.utcnow()
    s3_key = (
        f"hackernews/raw/"
        f"year={timestamp.year}/"
        f"month={timestamp.month:02d}/"
        f"day={timestamp.day:02d}/"
        f"{data.get('id')}.json"
    )

    try:
        print(f"Uploading to S3 → {s3_key}")
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=s3_key,
            Body=json.dumps(data)
        )
        print("Upload successful\n")
    except Exception as e:
        print("S3 upload failed:", e)