from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_BASE_DIR = BASE_DIR / "models" / "knowledge_base"


def list_knowledge_pdfs() -> list[str]:
    """
    Return the names of PDF files in the knowledge base folder.

    Later you can extend this into a full RAG pipeline (embed + search + answer).
    """
    if not KNOWLEDGE_BASE_DIR.exists():
        return []
    return [p.name for p in KNOWLEDGE_BASE_DIR.glob("*.pdf")]

