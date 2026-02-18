from typing import Optional


def generate_guidance(description: str, latitude: Optional[float] = None, longitude: Optional[float] = None) -> str:
    """
    Placeholder function.

    Later you can wire this up to OpenAI / Gemini / local LLM and include RAG over PDFs
    from `models/knowledge_base/`.
    """
    location_hint = ""
    if latitude is not None and longitude is not None:
        location_hint = f" (approx. location: {latitude:.5f}, {longitude:.5f})"

    return (
        "This is a demo response from the EEGA backend.\n\n"
        f"Reported situation{location_hint}:\n"
        f"- {description}\n\n"
        "Next: replace `generate_guidance` in `services/llm_service.py` with a real LLM call."
    )

