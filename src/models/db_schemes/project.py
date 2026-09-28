from typing import Optional

from pydantic import BaseModel, Field, field_validator


class Project(BaseModel):
    _id: Optional[str] = None
    project_id: str = Field(..., min_length=1)


    class Config:
        arbitrary_types_allowed = True