
from pydantic import BaseModel, Field


class ReportBase(BaseModel):
    email: str = Field(..., min_length=5, max_length=100, description="Email")
    status: str = Field(..., min_length=5, max_length=100, description="Status")
    type: str = Field(..., min_length=5, max_length=100, description="Type")


class ReportCreate(ReportBase):
    pass


class ReportRespone(ReportBase):
    id: int = Field(..., description="Unique report identifier")

    class Config:
        from_attributes = True


class ReportListResponse(BaseModel):
    reports: list[ReportRespone]  

    class Config:
        from_attributes = True  
