import uvicorn

from fastapi import FastAPI
from mangum import Mangum

from . import models
from .api import api_router
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=5000)
