from pathlib import Path
from typing import Generator, Optional
from pydantic import BaseModel
from backend.db.session import SessionLocal

BASE_PATH = Path(__file__).resolve().parent.parent

class TokenData(BaseModel):
    username: Optional[str] = None

def get_db() -> Generator:
    try:
        db = SessionLocal()
        db.current_user_id = None
        yield db
    finally:
        db.close()

