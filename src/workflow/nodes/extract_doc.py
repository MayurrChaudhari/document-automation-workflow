from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from src.config import settings
from src.workflow.state import State

model = ChatOpenAI(
    model=settings.OPENAI_EXTRACTION_MODEL,
    api_key=settings.OPENAI_API_KEY,
    temperature=0,
)


class ContractKeyTermsExtraction(BaseModel):
    """A contract key terms extraction."""

    contract_type: str = Field(
        description="The type of contract or title of the contract"
    )
    effective_date: str = Field(
        description="The effective date of the contract, e.g. '2021-01-01'"
    )
    parties_involved: str = Field(
        description="The parties involved in the contract, e.g. 'ABC Company, XYZ Company'"
    )
    term_duration: str = Field(
        description="The duration of the contract, in number of months."
    )
    governing_law: str = Field(
        description="The governing law of the contract, e.g. 'California'"
    )


class Extract(BaseModel):
    confidence: float = Field(
        "How confident are you about the extracted fields? range from 0.00 to 1.00"
    )
    fields: ContractKeyTermsExtraction


prompt = "- Provide required details about the contract."


def extract_document_node(state: State):
    """
    - Key Terms Extraction Node
    """
    document = state.get("document", "")

    model_with_structure = model.with_structured_output(Extract)
    response = model_with_structure.invoke(
        f"""## Document\n{document} \n\n ## Task for you\n{prompt}"""
    )
    response = response.__dict__

    Extract.model_validate(response)  # Guardrail

    return {
        "extracted_terms": response["fields"],
        "confidence": response["confidence"],
    }
