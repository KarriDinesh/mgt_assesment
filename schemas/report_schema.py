from pydantic import BaseModel
from typing import List

class Report(BaseModel):
    report: str
    open_questions: List[str]
    confidence: float

    