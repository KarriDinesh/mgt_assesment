from fastapi import FastAPI
import uuid
from pydantic import BaseModel

from graphs.research_graph import build_research_graph

app = FastAPI()

graph  = build_research_graph()

class ResearchRequest(BaseModel):
    topic: str

@app.post("/research")
def research(req: ResearchRequest):
    state = {
        'request_id': str(uuid.uuid4()),
        'topic': req.topic,
        'plan': '',
        'souces': [],
        'extracted_data': [],
        'comparison': None,
        'report': None,
        'open_questions': [],
        'confidence': 0.0,
        'status': 'started'
    }

    result = graph.invoke(state)
    return result    