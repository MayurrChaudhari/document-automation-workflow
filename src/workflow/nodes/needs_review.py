import asyncio

from src.services.db import update_needs_review
from src.workflow.state import State


def needs_review_node(state: State):
    """
    - Mark Extraction as needs review
    """
    asyncio.run(update_needs_review(state))
    print("Extracted fields need review.")
    return {
        "status": "needs_review",
    }
