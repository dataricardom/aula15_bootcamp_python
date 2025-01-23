from fastapi import FastAPI
from faker import Faker
import pandas as pd

app = FastAPI(debug=True)
fake = Faker()

@app.get("/")
async def hello_world():
    return "Hello World"

