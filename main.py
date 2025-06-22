from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

counter = {"value": 0}

@app.get("/count")
def get_count():
    return {"count": counter["value"]}

@app.post("/click")
def register_click():
    counter["value"] += 1
    return {"count": counter["value"]}

@app.post("/reset")
def reset_count():
    counter["value"] = 0
    return {"count": counter["value"]}
