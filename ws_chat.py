from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ..rag_pipeline import answer_query

router = APIRouter()

@router.websocket("/ws/chat")
async def chat_ws(ws: WebSocket):
    await ws.accept()

    try:
        while True:
            data = await ws.receive_json()
            question = data["question"]

            async def stream_cb(text):
                await ws.send_json({"type": "chunk", "text": text})

            full_answer = await answer_query(question, stream_callback=stream_cb)

            await ws.send_json({"type": "done", "answer": full_answer})

    except WebSocketDisconnect:
        print("Cliente desconectado.")
