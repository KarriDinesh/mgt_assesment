from model import generate_response
from schemas.report_schema import Report
import json

def writer_agent(state):

    prompt = f"""You are a research report writer. You will be given a research topic 
    {state['topic']}

    Analysis:
    {state['comparison']}

    Return JSON:
    {{
    "report": "text",
    "open_questions": ["question1", "question2", ...],
    "confidence":0.0
    }}
    """
    response = generate_response(prompt)

    try:
        response_json = json.loads(response)
        
        validated_report = Report(**response_json)

        state['report'] = validated_report.report
        state['open_questions'] = validated_report.open_questions
        state['confidence'] = validated_report.confidence
    except:
        state['report'] = response
        state['open_questions'] = []
        state['confidence'] = 0.5

    return state