from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.pj import router as pj_router
from routes.salary import router as salary_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(salary_router, prefix='/api/v1/salary', tags=['salary'])
app.include_router(pj_router, prefix='/api/v1/pj', tags=['pj'])


@app.get('/')
def _():
    return {"message": "Hello World"}
