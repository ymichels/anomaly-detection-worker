import boto3
import json
import time
from process_event import process_event
from events_db.events_db_redis import EventsDBRedis
from events_db.events_db_interface import EventsDBInterface
from anomaly_detection.anomaly_detection_interface import AnomalyDetectionInterface
from anomaly_detection.anomaly_detection import AnomalyDetection
from cloud_trail_event_model import CloudTrailEvent
from config.aws_config import REGION_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, QUEUE_URL
from config.general_config import WAIT_TIME_SECONDS, VISIBILITY_TIMEOUT


def events_handler():
    sqs = boto3.client('sqs', region_name=REGION_NAME, aws_access_key_id=AWS_ACCESS_KEY_ID,
                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    events_db: EventsDBInterface = EventsDBRedis()
    anomaly_detection: AnomalyDetectionInterface = AnomalyDetection()

    while True:
        response = sqs.receive_message(
            QueueUrl=QUEUE_URL,
            AttributeNames=['MessageAttributes'],
            VisibilityTimeout=VISIBILITY_TIMEOUT,
            WaitTimeSeconds=WAIT_TIME_SECONDS
        )

        if 'Messages' in response:
            for message in response['Messages']:
                event = json.loads(message['Body'])
                event = CloudTrailEvent(**event)
                print(f"Processing event: {event.eventID}")
                process_event(event, events_db, anomaly_detection)

                receipt_handle = message['ReceiptHandle']
                sqs.delete_message(QueueUrl=QUEUE_URL,
                                   ReceiptHandle=receipt_handle)
        else:
            print("No messages in the queue, waiting...")
            time.sleep(WAIT_TIME_SECONDS)


if __name__ == '__main__':
    events_handler()
