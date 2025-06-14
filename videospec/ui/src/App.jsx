import { useEffect, useRef, useState } from 'react';

function App() {
  const [status, setStatus] = useState('');
  const [firstBin, setFirstBin] = useState(0);
  const wsRef = useRef(null);

  useEffect(() => {
    fetch('/api/health')
      .then((r) => r.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus('error'));

    const ws = new WebSocket('ws://localhost:8000/api/fft');
    ws.onmessage = (event) => {
      const payload = JSON.parse(event.data);
      setFirstBin(payload.magnitudes[0] || 0);
    };
    wsRef.current = ws;
    return () => ws.close();
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">EasyRun Spectrum</h1>
      <p>Health: {status}</p>
      <p>First bin: {firstBin.toFixed(2)}</p>
    </div>
  );
}

export default App;
