
import logging
from fastapi import APIRouter, Request

router = APIRouter()

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

@router.get("/public_healthcheck")
def healthcheck():
    return "Alive."


