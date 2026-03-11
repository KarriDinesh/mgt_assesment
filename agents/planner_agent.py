from model import generate_response
import json

def planner_agent(state):

    prompt = f"""You are a research assistant. 
    Your task is to create a detailed plan for researching the topic: {state['topic']}.
    Create a ressearch plan.

    Return JSON:
    {{
        "plan": [
           'collect_sources', "extract_information", "compare_sources", "write_report"]        ]
    }}
    """

    response = generate_response(prompt)

    try:
        response_json = json.loads(response)
        state['plan'] = response_json['plan']
    except:
        state['plan'] = ['collect_sources', "extract_information", "compare_sources", "write_report"]
    
    return state