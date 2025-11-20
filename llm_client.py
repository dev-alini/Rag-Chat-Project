import os
import httpx

HF_API_KEY = os.getenv("HF_API_KEY")

async def generate_stream(prompt:str, model="tiiuae/falcon-7b-instruct", stream_callback=None):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    url = f"https://api-inference.huggingface.co/models/{model}"

    async with httpx.AsyncClient(timeout=200.0) as client:
        response = await client.post(url, headers=headers, json={"inputs": prompt})
        response.raise_for_status()

        result = response.json()
        text = result[0]["generated_text"]

        if stream_callback:
            await stream_callback(text)

        return text
