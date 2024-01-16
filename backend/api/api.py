from fastapi import APIRouter, Depends
from backend.api.controllers import auth_controller, user_controller, private, public, file_controller
from backend.services.auth_service import get_current_user

public_api_router = APIRouter(prefix="/api", tags=["Public Endpoints"])
public_api_router.include_router(public.router)
public_api_router.include_router(auth_controller.router)

private_api_router = APIRouter(prefix="/api", tags=["Private Endpoints"],dependencies=[Depends(get_current_user)])
private_api_router.include_router(private.router)
private_api_router.include_router(user_controller.router)
private_api_router.include_router(file_controller.router)



