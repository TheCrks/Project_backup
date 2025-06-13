from pydantic import BaseModel
from typing import List,Optional


class Logs(BaseModel):
    action: str
    itemId: str
    title: str
    url: str
    searchId: str
    timestamp: str
    rank : str

class LoggerResponse(BaseModel):
    result: str