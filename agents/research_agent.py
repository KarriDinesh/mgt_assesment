from tools.web_search import search_sources
from tools.mgt_tool import fetch_mgt_content

def research_agent(state):
    topic = state['topic']
    sources = search_sources(topic)
    if 'mgt' in topic.lower():
        mgt_content = fetch_mgt_content()
        state['mgt_information'] = mgt_content
    state['sources'] = sources
    return state