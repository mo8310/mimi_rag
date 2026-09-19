from helpers.config import get_settings, Settings
from.BaseController import BaseController
from fastapi import UploadFile

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        
        
        
    def validate_uploaded_file(self, file: UploadFile):
        # Validate file type
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False
        
        # Validate file size
        if file.size > self.app_settings.FILE_MAX_SIZE_MB * 1024 * 1024:
            return False
        
        return True