from cloud_trail_event_model import CloudTrailEvent
from events_db.events_db_interface import EventsDBInterface
from config.redis_config import REDIS_HOST, REDIS_PORT, CLOUDTRAIL_HASHING_FILEDS
import redis
import hashlib
import json
from logging import Logger


class EventsDBRedis(EventsDBInterface):
    def __init__(self, logger:Logger) -> None:
        self.logger = logger
        self.redis_client = redis.StrictRedis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True
        )

    def __get_event_hash_key(self, event: CloudTrailEvent):
        event_dict = event.to_json()
        hash_str = ''.join([str(event_dict[field])
                            for field in CLOUDTRAIL_HASHING_FILEDS])
        hash_key = hashlib.md5(hash_str.encode()).hexdigest()
        return hash_key

    def write_event(self, event: CloudTrailEvent):
        self.logger.info(f'Writing event {event.eventID} to the DB')
        event_json = json.dumps(event.to_json())
        hash_key = self.__get_event_hash_key(event)
        self.redis_client.hset(hash_key, 'data', event_json)

    def write_score(self, event: CloudTrailEvent, score: float):
        self.logger.info(f'Writing score of event {event.eventID} to the DB')
        hash_key = self.__get_event_hash_key(event)
        self.redis_client.hset(hash_key, 'score', score)

    def read_score(self, event: CloudTrailEvent) -> float:
        self.logger.info(f'Searching for score of {event.eventID} in the DB')
        hash_key = self.__get_event_hash_key(event)
        return self.redis_client.hget(hash_key, 'score')
