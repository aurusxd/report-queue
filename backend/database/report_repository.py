from database.models.report import Report
from schemas.report_schema import ReportCreate
from sqlalchemy.orm import Session


class ReportRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_all(self) -> list[Report]:
        return self.db.query(Report).all()

    def get_by_id(self, report_id: int) -> Report | None:
        return self.db.query(Report).filter(Report.id == report_id).first()


    def create(self, data: ReportCreate) -> Report:
        report = Report(**data.model_dump())
        self.db.add(report)
        self.db.commit()
        self.db.refresh(report)
        return report

    

