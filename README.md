# Audio-Tool-Ideas

This project contains the `videospec` application. Before running the code you need to install its dependencies.

## Python packages

Install the Python dependencies using [Poetry](https://python-poetry.org/):

```bash
poetry install
```

Alternatively you can use `pip` if a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

## Node packages

The frontend code lives in `videospec/ui`. Install its Node packages by running:

```bash
cd videospec/ui
npm install
```

When a `package-lock.json` file is present, use `npm ci` for faster
and reproducible installs:

```bash
npm ci
```
