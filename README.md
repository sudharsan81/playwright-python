# API E2E Tests

This repository demostrates api tests using native playwright python library. Test sends XML payload over HTTP.

## Pre-requisites

- python 3
- pip 3

## Preparation

> Ensure you are in the home directory of this repo.

> All the local foler names are set by convention.

1. Use Python Virtual environment
```bash
source pw/bin/activate
```

2. Run the test
```bash
pytest -v pw/test_send_xml_api.py
```
