# demo-app

A simple FastAPI app used as the target for the v2a voice-to-action demo.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | App info |
| GET | `/health` | Liveness check |
| POST | `/echo` | Returns the message you send |
| POST | `/greet` | Returns a greeting for a name |

## Run

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Test

```bash
pytest test_app.py -v
```
