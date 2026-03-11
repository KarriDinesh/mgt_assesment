from typing import Optional, List, TypedDict

#schema neeeds to be followed for the research state to be stored in the database
class ResearchState(TypedDict):
    request_id : str
    topic : str
    plan: List[str]
    sources : List[str]
    extracted_data : List[str]
    comparison : Optional[str]
    report : Optional[str]
    open_questions : List[str]
    confidence:float
    mgt_information: str
    status: str