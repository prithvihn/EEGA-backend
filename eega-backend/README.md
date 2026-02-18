## EEGA Backend (FastAPI)

This folder contains the **emergency assistant backend** built with **FastAPI**.

- `main.py` – FastAPI app entrypoint, CORS setup, and router registration
- `routes/emergency.py` – `/emergency` endpoint that will call the LLM service
- `routes/location.py` – `/location/nearby` endpoint for nearby places lookup
- `services/llm_service.py` – placeholder LLM guidance generator
- `services/rag_service.py` – placeholder for RAG over PDFs in `models/knowledge_base/`
- `services/places_service.py` – placeholder for nearby emergency places
- `models/knowledge_base/` – put your emergency protocol PDFs here
- `.env` – environment variables (API keys, etc.)

Setup and run:

```bash
cd eega-backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

