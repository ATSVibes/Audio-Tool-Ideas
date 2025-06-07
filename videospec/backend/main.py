"""FastAPI entry point (placeholder)"""

from fastapi import FastAPI

app = FastAPI(title="EasyRun Spectrum API")

@app.get("/api/health")
async def health():
    return {"status": "ok"}
