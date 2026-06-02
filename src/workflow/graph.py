from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph

from .edges import check_confidence
from .nodes import (
    complete_node,
    extract_document_node,
    needs_review_node,
    read_document_node,
)
from .state import State

workflow = StateGraph(State)

workflow.add_node(read_document_node)
workflow.add_node(extract_document_node)
workflow.add_node(complete_node)
workflow.add_node(needs_review_node)

workflow.add_edge(START, "read_document_node")
workflow.add_edge("read_document_node", "extract_document_node")

workflow.add_conditional_edges(
    "extract_document_node",
    check_confidence,
    ["complete_node", "needs_review_node"],
)

workflow.add_edge("extract_document_node", END)

checkpointer = InMemorySaver()
graph = workflow.compile(checkpointer=checkpointer)
