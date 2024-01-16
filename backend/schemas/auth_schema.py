from pydantic import BaseModel
from typing import Annotated, Union

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None


class UserResponse(BaseModel):
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    is_active: Union[bool, None] = None


class UserInDB(UserResponse):
    hashed_password: str