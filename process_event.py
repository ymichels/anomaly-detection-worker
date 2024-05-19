from cloud_trail_event_model import CloudTrailEvent
from events_db.events_db_interface import EventsDBInterface
from anomaly_detection.anomaly_detection_interface import AnomalyDetectionInterface
from logging import Logger

def process_event(event: CloudTrailEvent, events_db: EventsDBInterface, anomaly_detection: AnomalyDetectionInterface, logger:Logger):
    score = events_db.read_score(event)
    if score is not None:
        logger.info(f'Event {event.eventID}: {score}')
        return

    score = anomaly_detection.detect_anomaly(event)
    events_db.write_score(event=event, score=score)
    if score > 0:
        events_db.write_event(event=event)
