from .embeddings import embed_texts
from .vector_store import FaissStore
from .db import fetch_relevant_rows
from .llm_client import generate_stream

_vector_store = None

def init_vector_store(dim):
    global _vector_store
    _vector_store = FaissStore(dim)

async def index_sql_table(sql_query:str, text_field="content"):
    rows = fetch_relevant_rows(sql_query)
    texts = [r[text_field] for r in rows]
    embs = embed_texts(texts)

    metas = [
        {"id": r["id"], "text": r[text_field]}
        for r in rows
    ]

    _vector_store.add(embs, metas)

async def answer_query(user_query, k=5, stream_callback=None):
    q_emb = embed_texts([user_query])
    hits = _vector_store.search(q_emb, k=k)[0]

    context = "\n".join([f"[{h['meta']['id']}] {h['meta']['text']}" for h in hits])

    prompt = f"""
Use o contexto abaixo para responder:

CONTEXT:
{context}

PERGUNTA:
{user_query}

RESPOSTA:
"""

    answer = await generate_stream(prompt, stream_callback=stream_callback)
    return answer
