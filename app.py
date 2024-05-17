import boto3
import json
import time
from queue_mock import SQS
from process_event import process_event
from events_db.events_db_redis import EventsDBRedis
from events_db.events_db_interface import EventsDBInterface
from anomaly_detection.anomaly_detection_interface import AnomalyDetectionInterface
from anomaly_detection.anomaly_detection import AnomalyDetection
from cloud_trail_event_model import CloudTrailEvent
from config.aws_config import REGION_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
# AWS credentials and region configuration
# AWS_ACCESS_KEY_ID = 'your_access_key_id'
# AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'
# AWS_REGION = 'your_aws_region'


def events_handler():
    # Get the SQS queue resource
    sqs = boto3.client('sqs', region_name=REGION_NAME, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    # sqs = boto3.client('sqs')
    # sqs = SQS()
    events_db:EventsDBInterface = EventsDBRedis()
    anomaly_detection:AnomalyDetectionInterface = AnomalyDetection()

    # Replace 'YOUR_QUEUE_URL' with the URL of your SQS queue
    queue_url = 'https://sqs.eu-north-1.amazonaws.com/767398004368/orca-excercise'

    # Number of seconds to wait for a message (adjust as needed)
    wait_time_seconds = 1

    # Number of seconds to lock the message for processing (adjust as needed)
    visibility_timeout = 30

    while True:
        # Receive a message from the queue with message locking
        response = sqs.receive_message(
            QueueUrl=queue_url,
            AttributeNames=['MessageAttributes'],
            VisibilityTimeout=visibility_timeout,
            WaitTimeSeconds=wait_time_seconds
        )

        # Check if there are any messages in the queue
        if 'Messages' in response:
            for message in response['Messages']:
                # Process the message data (replace with your processing logic)
                event = json.loads(message['Body'])
                event = CloudTrailEvent(**event)
                print(f"Processing event: {event.eventID}")
                process_event(event, events_db, anomaly_detection)
                
                # Delete the message from the queue after processing
                receipt_handle = message['ReceiptHandle']
                sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
        else:
            print("No messages in the queue, waiting...")
            time.sleep(wait_time_seconds)

if __name__ == '__main__':
    events_handler()