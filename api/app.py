from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def _():
    return {"message": "Hello World"}