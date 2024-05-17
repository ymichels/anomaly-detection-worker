import random
from cloud_trail_event_model import CloudTrailEvent


class SQS:
    def receive_message(*args, **kwargs):
        random_number = random.randint(0, 1)
        if random_number == 0:
            return {}
        return {
            'Messages': [
                CloudTrailEvent(requestID='string', eventID="1", roleID="string",
                                eventType="string2", eventTime="string", affectedAssets=["string"]),
                CloudTrailEvent(requestID='string', eventID="2", roleID="string",
                                eventType="string3", eventTime="string", affectedAssets=["string"]),
                CloudTrailEvent(requestID='string', eventID="3", roleID="string",
                                eventType="string4", eventTime="string", affectedAssets=["string"]),
            ]
        }

    def delete_message(*args, **kwargs):
        pass
