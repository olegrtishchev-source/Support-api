from fastapi import FastAPI

app = FastAPI(title="Support API")


@app.get("/health")
def health():
    return {"status": "ok"}
