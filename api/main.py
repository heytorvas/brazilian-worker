from errors import error_handler
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resources.routes.clt import router as clt_router
from resources.routes.compare import router as compare_router
from resources.routes.pj import router as pj_router
from resources.routes.thirteenth import router as thirteenth_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

error_handler(app)

app.include_router(clt_router, prefix="/api/v1/clt", tags=["clt"])
app.include_router(pj_router, prefix="/api/v1/pj", tags=["pj"])
app.include_router(compare_router, prefix="/api/v1/compare", tags=["compare"])
app.include_router(thirteenth_router, prefix="/api/v1/thirteenth", tags=["thirteenth"])


@app.get("/")
def _():
    return {"message": "Hello World"}
