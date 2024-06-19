# app.py
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/hello")
def read_root():
    return {"Hello": "Admin"}


handler = Mangum(app)
