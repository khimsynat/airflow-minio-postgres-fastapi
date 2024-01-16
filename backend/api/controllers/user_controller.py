
import logging
from fastapi import APIRouter, Request, Depends, HTTPException, status
from backend.crud.base import CRUDBase
from backend.schemas import schemas
from backend.api.deps import get_db
from backend.models import models
from sqlalchemy.orm import Session
from backend.crud import crud
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

@router.get("/users", response_model=schemas.User)
def get_users(db: Session = Depends(get_db)):
    users=CRUDBase(models.User).get_multi(db)
    return JSONResponse(status_code=status.HTTP_200_OK, content={'users': jsonable_encoder(users)})