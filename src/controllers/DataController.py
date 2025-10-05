from .BaseController import BaseController
from fastapi import UploadFile

class DataController(BaseController):
    
    self.size_scale = 1024 * 1024  # Convert MB to bytes
    
    def __init__(self):
        super().__init__()
        
    def validate_file(self, file: UploadFile) -> bool:
        if file.content_type not in self.app_settings.FILE_ALLOWED_EXTENSTIONS:
            return False
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False
        
        return True