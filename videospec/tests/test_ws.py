import asyncio
from fastapi.testclient import TestClient

from videospec.backend.main import app
import videospec.backend.audio_rt as audio_rt


async def fake_fft_frames():
    for i in range(2):
        yield {"time": 0.0, "magnitudes": [i]}


def test_websocket_fft(monkeypatch):
    monkeypatch.setattr(audio_rt, "fft_frames", fake_fft_frames)
    client = TestClient(app)
    with client.websocket_connect("/api/fft") as ws:
        data = ws.receive_json()
        assert data["magnitudes"] == [0]
        data2 = ws.receive_json()
        assert data2["magnitudes"] == [1]
