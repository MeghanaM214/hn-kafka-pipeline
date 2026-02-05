import json
import time
import requests
from kafka import KafkaProducer

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

def get_top_story_ids():
    response = requests.get(TOP_STORIES_URL)
    return response.json()[:5]  # take only 5 to keep it simple

def get_story(story_id):
    response = requests.get(ITEM_URL.format(story_id))
    return response.json()

while True:
    print("Fetching top stories...")
    for story_id in get_top_story_ids():
        story = get_story(story_id)
        if story:
            producer.send("hackernews", story)
            print(f"Sent story ID: {story_id}")
        time.sleep(1)

    print("Sleeping for 30 seconds...\n")
    time.sleep(30)