from langgraph.graph import START, END, StateGraph, MessagesState
from typing import Dict, TypedDict, Optional
import datetime
import chain
import transcript

log_created_at = datetime.datetime.now().strftime("%d-%m-%Y--%H-%M-%S")

class GraphState(TypedDict):
    datetime: Optional[str] = None

workflow = StateGraph(GraphState)

def transcribe(state):
    datetime, input_file = transcript.transcriber()
    return datetime, input_file

def summarize(state, datetime, input_file):
    dt = state
    chain.summarize(datetime, input_file)

workflow.add_edge(START, "transcription")
workflow.add_node("transcription", transcribe)

workflow.add_edge("transcription", "call_model")
workflow.add_node("call_model", summarize)

workflow.add_edge("call_model", END)

app = workflow.compile()
config = {"configurable": {"thread_id": "xyz"}}

app.invoke(input = {"datetime": log_created_at}, config = config)



