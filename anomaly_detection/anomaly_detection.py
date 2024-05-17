from cloud_trail_event_model import CloudTrailEvent
from anomaly_detection.anomaly_detection_interface import AnomalyDetectionInterface
import random
class AnomalyDetection(AnomalyDetectionInterface):
    def detect_anomaly(self, event:CloudTrailEvent) -> float:
        print(f'Detecting anomalies in event {event.eventID}...')
        # I assume there's a good chance that its not an anomaly
        random_number = random.randint(0, 1)
        if random_number == 0:
            return random_number
        return random.random()
        
        