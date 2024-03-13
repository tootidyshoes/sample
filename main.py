import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/alive-check")
def read_root():
    return {"message": "Service is up and running."}
