from abc import ABC, abstractmethod
from cloud_trail_event_model import CloudTrailEvent


class AnomalyDetectionInterface(ABC):
    @abstractmethod
    def detect_anomaly(self, event: CloudTrailEvent) -> float:
        """
        Detects anomalys in a CloudTrailEvent object.

        Parameters:
        - event (CloudTrailEvent): The CloudTrailEvent object.
        """
        pass
