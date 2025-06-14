"""FastAPI entry point for EasyRun Spectrum Analyzer."""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from . import audio_rt

app = FastAPI(title="EasyRun Spectrum API")


@app.get("/api/health")
async def health():
    return {"status": "ok"}


@app.websocket("/api/fft")
async def fft_stream(ws: WebSocket):
    await ws.accept()
    try:
        async for frame in audio_rt.fft_frames():
            await ws.send_json(frame)
    except WebSocketDisconnect:
        pass
