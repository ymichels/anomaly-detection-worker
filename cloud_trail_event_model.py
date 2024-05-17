from pydantic import BaseModel
from typing import List
class CloudTrailEvent(BaseModel):
    requestID: str
    eventID: str
    roleID: str
    eventType: str
    eventTime: str
    affectedAssets: List[str] 