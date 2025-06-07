# EasyRun Video Spectrum Analyzer

This repository contains a prototype of the EasyRun Video Spectrum Analyzer as
outlined in the design document. It visualizes audio spectra in real time and
can overlay the visualization on existing videos.

## Development

The backend uses **FastAPI** and exposes both REST and WebSocket endpoints. The
frontend is a small **React** app built with **Vite**. During development you will
run both servers:

```bash
# Backend (Python 3.11)
uvicorn videospec.backend.main:app --reload

# Frontend (inside `videospec/ui`)
npm install  # first time only
npm run dev
```

The React dev server proxies `/api/*` and WebSocket connections to the backend.
Open <http://localhost:5173> to see the app. It should report the API health
check and display the first FFT bin streamed from `/api/fft`.

## Tests

Run the Python test suite with:

```bash
pytest
```
