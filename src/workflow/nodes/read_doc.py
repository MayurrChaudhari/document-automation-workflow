from pypdf import PdfReader

from src.workflow.state import State


def read_document_node(state: State):
    """
    - Document parser node
    """

    path = state.get("document_path", "")

    if path.endswith(".pdf"):
        reader = PdfReader(path)
        pages = reader.pages
        pages_text = [page.extract_text() for page in pages]
        return {
            "document": "\n\n".join(pages_text),
        }
    elif path.endswith(".txt"):
        with open(path, "rb") as file:
            return {
                "document": file.read(),
            }
