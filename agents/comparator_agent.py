from model import generate_response

def comparator_agent(state):
    insights = [x['insights'] for x in state['extracted_data']]


    prompt=f"""Compare findings from multiple sources.

    Find:
    1. Agreements
    2. Disagreements
    3. Unique insights

    Sources data:
    {insights}
    """
    response = generate_response(prompt)
    state['comparison'] = response

    return state