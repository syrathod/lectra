from langgraph.graph import START, END, StateGraph, MessagesState
from typing import Dict, TypedDict, Optional
import datetime
from chain import chain
from transcript import transcriber
from scheduler import scheduler

log_created_at = datetime.datetime.now().strftime("%d-%m-%Y--%H-%M-%S")

class GraphState(TypedDict):
    datetime: Optional[str] = None
    log: Optional[str] = None

workflow = StateGraph(GraphState)

def transcribe(state):
    print("\n[*] Transcribing...")
    input_file = transcriber.transcribe(state["datetime"])
    return {"log": input_file}

def summarize(state):
    print(f"[*] Summary (at {state["datetime"]}): \n")
    dt = state["datetime"]
    input_file = state["log"]
    chain.summarize(dt, input_file)

def schedule(state):
    scheduler.schedule()
    new_log_created_at = datetime.datetime.now().strftime("%d-%m-%Y--%H-%M-%S")
    return {"datetime": new_log_created_at} 

workflow.add_edge(START, "transcription")
workflow.add_node("transcription", transcribe)

workflow.add_edge("transcription", "call_model")
workflow.add_node("call_model", summarize)

workflow.add_edge("call_model", "scheduler")
workflow.add_node("scheduler", schedule)

workflow.add_edge("scheduler", "transcription")

app = workflow.compile()
config = {"recursion_limit": 999}

inputs = {"datetime": log_created_at}

app.invoke(input = inputs, config = config)



