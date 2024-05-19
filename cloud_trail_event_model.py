from pydantic import BaseModel
from typing import List
import json

class CloudTrailEvent(BaseModel):
    requestID: str
    eventID: str
    roleID: str
    eventType: str
    eventTime: str
    affectedAssets: List[str]
    
    def to_json(self):
        return {
            "requestID": self.requestID,
            "eventID": self.eventID,
            "roleID": self.roleID,
            "eventType": self.eventType,
            "eventTime": self.eventTime,
            "affectedAssets": self.affectedAssets,
        }
