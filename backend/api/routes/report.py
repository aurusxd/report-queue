


from typing import Annotated

from database.core import get_db
from fastapi import APIRouter, Depends, status
from schemas.report_schema import ReportCreate, ReportRespone
from services.report_service import ReportService
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/reports",
    tags=['reports']
)

@router.get(
    "", response_model=list[ReportRespone],status_code=status.HTTP_200_OK
    )
def get_report(db: Annotated[Session, Depends(get_db)]):
    service = ReportService(db)
    return service.get_all()

@router.get('/{report_id}', response_model=ReportRespone, status_code=status.HTTP_200_OK)
def get_report_by_id(report_id: int, db: Annotated[Session, Depends(get_db)]):
    service = ReportService(db)
    return service.get_by_id(report_id)

@router.post('/create',status_code=status.HTTP_200_OK)
def create_report(data: ReportCreate, db: Annotated[Session, Depends(get_db)]) -> ReportRespone | None:
    service = ReportService(db)
    return service.create_report(data)


