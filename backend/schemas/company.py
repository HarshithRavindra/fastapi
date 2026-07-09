
from pydantic import BaseModel
from typing import Optional
from .job import JobResponse

class CompanyBase(BaseModel):
    name: str

class CompanyCreate(CompanyBase):
    email: str
    phone: str
    location: str

class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None

class CompanyResponse(CompanyBase):
    id: int
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    jobs: list[JobResponse]

    class Config:
        from_attributes = True

