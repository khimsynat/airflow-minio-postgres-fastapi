from fastapi import FastAPI, Request, APIRouter, File, UploadFile
from backend.services.file_service import get_object, put_object
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    
    data = put_object("images", file)
    if data:
        return {'data': data}
    else:
        return {"msg": "Error during save file"}

@router.get("/image/{filename}")
async def get_file(filename:str,request: Request):

    response = get_object("images", filename)
    if response:
        return StreamingResponse(content=response, media_type="image/jpeg")
    else:
        return {"msg": "File not found."}
