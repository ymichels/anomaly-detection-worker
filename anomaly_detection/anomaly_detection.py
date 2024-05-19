from cloud_trail_event_model import CloudTrailEvent
from anomaly_detection.anomaly_detection_interface import AnomalyDetectionInterface
import random
from logging import Logger

class AnomalyDetection(AnomalyDetectionInterface):
    
    def __init__(self, logger: Logger) -> None:
        self.logger = logger
        
    def detect_anomaly(self, event: CloudTrailEvent) -> float:
        self.logger.info(f'Detecting anomalies in event {event.eventID}...')
        # I assume there's a 50% chance that its not an anomaly
        random_number = random.randint(0, 1)
        if random_number == 0:
            return random_number
        return random.random()
