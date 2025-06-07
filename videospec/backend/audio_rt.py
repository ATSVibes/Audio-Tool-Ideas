"""Realtime audio capture and FFT utilities."""

from __future__ import annotations

import asyncio
import time
from typing import AsyncGenerator, Optional

import numpy as np

try:
    import sounddevice as sd
except Exception:  # pragma: no cover - fallback when sounddevice fails
    sd = None


async def audio_frames(
    blocksize: int = 1024,
    samplerate: int = 48_000,
    device: Optional[int] = None,
) -> AsyncGenerator[np.ndarray, None]:
    """Yield raw audio frames asynchronously.

    If ``sounddevice`` is unavailable, this yields random noise frames. This
    function does not enforce real-time guarantees but is sufficient for
    prototyping and unit tests.
    """

    q: asyncio.Queue[np.ndarray] = asyncio.Queue()

    if sd is not None:
        def callback(indata, frames, time_info, status):
            if status:
                print("Audio status", status)
            q.put_nowait(indata[:, 0].copy())

        stream = sd.InputStream(
            channels=1,
            samplerate=samplerate,
            blocksize=blocksize,
            device=device,
            callback=callback,
        )
        stream.start()
    else:  # pragma: no cover - fall back to synthetic data
        stream = None

        async def fake_stream():
            period = blocksize / samplerate
            while True:
                await asyncio.sleep(period)
                q.put_nowait(np.random.rand(blocksize))

        asyncio.create_task(fake_stream())

    try:
        while True:
            frame = await q.get()
            yield frame
    finally:
        if stream is not None:
            stream.stop()
            stream.close()


async def fft_frames(
    blocksize: int = 1024,
    samplerate: int = 48_000,
    device: Optional[int] = None,
) -> AsyncGenerator[dict, None]:
    """Yield FFT magnitudes for incoming audio frames."""

    async for frame in audio_frames(blocksize, samplerate, device):
        mags = np.abs(np.fft.rfft(frame)).astype(float)
        yield {
            "time": time.time(),
            "magnitudes": mags.tolist(),
        }
