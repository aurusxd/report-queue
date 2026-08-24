from fastapi import HTTPException, status

from database.report_repository import ReportRepository
from sqlalchemy.orm import Session
from database.models.report import Report
from schemas.report_schema import ReportRespone, ReportCreate

class ReportService:
    def __init__(self, db: Session):
        self.repository = ReportRepository(db)

    def get_all_reports(self) -> list[Report]:
        reports = self.repository.get_all()
        return [ReportRespone.model_validate(rep) for rep in reports]

    def get_by_id(self,report_id: int) -> ReportRespone | None:
        report = self.repository.get_by_id(report_id)
        if not report:
            return HTTPException(
                status_code=status.HTTP_400_NOT_FOUND,
                detail=f"Report with id {report_id} not found"
            )
        return ReportRespone.model_validate(report)

    def create_report(self, data: ReportCreate) -> ReportRespone | None:
        report = self.repository.create(data)
        if not report:
            return HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Report not created"
            )
        return ReportRespone.model_validate(report)

        