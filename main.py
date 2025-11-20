from fastapi import FastAPI
from .api.ws_chat import router as ws_router
from .embeddings import load_model
from .rag_pipeline import init_vector_store

app = FastAPI()
app.include_router(ws_router)

@app.on_event("startup")
async def startup_event():
    model = load_model()
    dim = model.get_sentence_embedding_dimension()
    init_vector_store(dim)
    print(f"🧠 Embeddings carregados. Dimensão: {dim}")
