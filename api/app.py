from fastapi import FastAPI

from api.routes.salary import router as salary_router

app = FastAPI()

app.include_router(salary_router, prefix='/api/v1/salary', tags=['salary'])

@app.get('/')
def _():
    return {"message": "Hello World"}
