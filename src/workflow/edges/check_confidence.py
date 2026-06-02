from src.config import settings
from src.workflow.state import State


def check_confidence(state: State):
    """Decide if we should mark the task completed or needs a review?"""

    confidence = state["confidence"]

    if confidence > settings.EXTRACTION_THRESHOLD:
        return "complete_node"
    else:
        return "needs_review_node"
