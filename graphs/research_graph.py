from langgraph.graph import StateGraph, END
from schemas.research_state import ResearchState
from agents.writer_agent import writer_agent
from agents.comparator_agent import comparator_agent
from agents.research_agent import research_agent
from agents.extractor_agent import extractor_agent
from agents.planner_agent import planner_agent

from tools.storage import save_result

def confidence_route(state):
    if state['confidence'] < 0.6:
        state['status'] = 'low confidence, needs_human_review'
    else:
        state['status'] = 'complete'
    save_result(state['request_id'], state)
    return state

def build_research_graph():
    graph = StateGraph(ResearchState)

    graph.add_node('planner', planner_agent)
    graph.add_node('research', research_agent)
    graph.add_node('extract', extractor_agent)
    graph.add_node('compare', comparator_agent)
    graph.add_node('write', writer_agent)
    graph.add_node('confidence', confidence_route)

    graph.set_entry_point('planner')
    graph.add_edge('planner', 'research')
    graph.add_edge('research', 'extract')
    graph.add_edge('extract', 'compare')
    graph.add_edge('compare', 'write')
    graph.add_edge('write', 'confidence')
    graph.add_edge('confidence', END)


    comp = graph.compile()
    print(comp.get_graph().draw_ascii())
    return comp



