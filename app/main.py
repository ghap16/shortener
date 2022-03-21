import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from .api import api_router
from .config import settings
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(openapi_prefix=settings.openapi_prefix)

app.include_router(api_router)

handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=5000)
