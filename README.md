# API E2E Tests

This repository demostrates api tests using native playwright python library. Test sends XML payload over HTTP.

## Pre-requisites

- python 3
- pip 3

## Preparation

> Ensure you are in the home directory of this repo.
> All the local foler names are set by convention.

1. Create Virtual Environment
```bash
python3 -m venv playwright-env
```

2. Use Python Virtual environment
```bash
source playwright-env/bin/activate
```

3. Install pytest and playwright from Virtual environment prompt
```bash
pip install playwright
pip install pytest
```

2. Run the test
```bash
pytest -v test_send_xml_api.py
```
