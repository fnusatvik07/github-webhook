from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Webhook server is running"}

@app.post("/webhook")
async def github_webhook(request: Request):
    event = request.headers.get("X-GitHub-Event")
    payload = await request.json()
    print(f"🔔 Received event: {event}")
    print(payload)
    return {"status": "ok"}
