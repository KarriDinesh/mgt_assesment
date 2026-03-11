from model import generate_response
from tools.web_fetcher import fetch_content


def extractor_agent(state):
    extraction = []
    mgt_info = state.get('mgt_information')
    for src in state['sources']:
        content = fetch_content(src)
        if content:
            prompt = f"Extract the relevant information from the following source:\n\n{content}\n\n Additional Domain Knowledge: {mgt_info}\n\nReturn bullet points:"
            response = generate_response(prompt)
            extraction.append( {'source': src, 'insights': response})
    state['extracted_data'] = extraction
    return state