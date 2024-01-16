import logging

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from starlette.middleware.cors import CORSMiddleware

from backend.api.api import public_api_router, private_api_router
from backend.core.config import settings
from backend.models import models
from backend.db.session import engine
logging.basicConfig(level="INFO")

# Dependency to create table from all of schemas.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,docs_url="/api/docs", openapi_url="/api",
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(public_api_router)
app.include_router(private_api_router)



