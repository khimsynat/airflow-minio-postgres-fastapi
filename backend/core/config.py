from functools import lru_cache
import os
from dotenv import load_dotenv
from typing import Any, Dict, List, Optional
from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator, constr

load_dotenv()

BaseSettings.Config.arbitrary_types_allowed = True

class NotNoneStr(constr(strip_whitespace=True, min_length=1)):
    pass

class Settings(BaseSettings):
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = 'chs-datastore'
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    API_KEY: NotNoneStr = os.environ.get("API_KEY")
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    
    MINIO_ENDPOINT=os.environ.get("MINIO_ENDPOINT")
    MINIO_PORT=os.environ.get("MINIO_PORT")
    MINIO_ACCESS_KEY=os.environ.get("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY=os.environ.get("MINIO_SECRET_KEY")

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

class Config:
        case_sensitive = True

# New decorator for cache
@lru_cache()
def get_settings():
    return Settings(),


settings = Settings()
