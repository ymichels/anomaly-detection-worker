from abc import ABC, abstractmethod
from cloud_trail_event_model import CloudTrailEvent


class EventsDBInterface(ABC):
    @abstractmethod
    def write_event(self, event: CloudTrailEvent):
        """
        Writes an event to the DB.

        Parameters:
        - event (CloudTrailEvent): The CloudTrailEvent object.
        - score (float): The anomaly score of the event.
        - save_event_details (bool): Indicates whether to preserve event details
        """
        pass

    @abstractmethod
    def write_score(self, event: CloudTrailEvent, score: float):
        """
        Writes a score for an event to the DB.

        Parameters:
        - event (CloudTrailEvent): The CloudTrailEvent object.
        - score (float): The anomaly score of the event.
        """
        pass

    @abstractmethod
    def read_score(self, event: CloudTrailEvent) -> float:
        """
        Reads a score of an event from the DB. Returns -1 if not found.

        Parameters:
        - event (CloudTrailEvent): The CloudTrailEvent object.
        """
        pass
