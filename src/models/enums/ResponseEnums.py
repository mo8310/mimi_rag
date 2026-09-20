from enum import Enum

class ResponseSignal(Enum):
    FILE_UPLOAD_SUCCESS = "Success"
    FILE_UPLOAD_FAILED = "File upload failed"
    FILE_TYPE_NOT_SUPPORTED = "File type not allowed"
    FILE_SIZE_EXCEEDED = "File size exceeds maximum allowed size"
    FILE_VALIDATION_SUCCESS = "File is valid"