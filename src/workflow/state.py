from typing import Literal

from pydantic import UUID4
from typing_extensions import TypedDict


class State(TypedDict):
    confidence: float
    document_path: str
    document: str
    extracted_terms: dict
    status: Literal["complete", "needs_review"]
    correlation_id: UUID4
    transitions: list = ["start"]
