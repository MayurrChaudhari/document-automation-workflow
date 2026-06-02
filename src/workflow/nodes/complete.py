import asyncio

from src.services.db import update_complete
from src.workflow.state import State


def complete_node(state: State):
    """
    - Mark Extraction as complete
    """
    asyncio.run(update_complete(state))
    print("Extraction Completed Sucessfully")
    return {
        "status": "Complete",
    }
