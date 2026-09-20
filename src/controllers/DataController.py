import uuid
import random
import os
import string
import re
from helpers.config import get_settings, Settings
from models.enums.ResponseEnums import ResponseSignal
from.BaseController import BaseController
from fastapi import UploadFile
from models.enums.ResponseEnums import ResponseSignal
from .ProjectController import ProjectController

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        
        
        
    def validate_uploaded_file(self, file: UploadFile):
        # Validate file type
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        # Validate file size
        if file.size > self.app_settings.FILE_MAX_SIZE_MB * 1024 * 1024:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value
        
        return True, ResponseSignal.FILE_VALIDATION_SUCCESS.value
    
    def generate_unique_filename(self, orig_file_name: str, project_id: str):
        
        random_KEY = uuid.uuid4().hex
        project_path = ProjectController().get_project_path(project_id=project_id)
        
        cleaned_file_name = self.get_cleaned_file_name(orig_file_name=orig_file_name)
        
        new_file_path = os.path.join(project_path, random_KEY + "_" +cleaned_file_name
                                     )
        while os.path.exists(new_file_path):
            random_KEY = uuid.uuid4().hex
            new_file_path = os.path.join(project_path, random_KEY + "_" + cleaned_file_name)    

        return new_file_path
        
        
    def  get_cleaned_file_name(self, orig_file_name: str):
        # Remove special characters and spaces from the filename
        cleaned_file_name = re.sub(r'[^\w.]', '_', orig_file_name.strip())
        return cleaned_file_name
        