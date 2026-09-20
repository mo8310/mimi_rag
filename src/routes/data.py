from fastapi import FastAPI, APIRouter, Depends, UploadFile, File, status
from fastapi.responses import JSONResponse
import aiofiles
import os
from helpers.config import get_settings, Settings
from controllers import DataController
from controllers import ProjectController
from models.enums.ResponseEnums import ResponseSignal
import logging

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile = File(...), 
                                       app_settings=Depends(get_settings)):
    
    data_controller = DataController()
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)
    
    if not is_valid:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"Signal": result_signal})
    
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = data_controller.generate_unique_filename(orig_file_name=file.filename, project_id=project_id)
    
    
    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
              await f.write(chunk)
    except Exception as e:
        logger.error(f"Error occurred while saving the file: {str(e)}")
        
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"Signal": ResponseSignal.FILE_UPLOAD_FAILED.value, "Error": str(e)})
    
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value})