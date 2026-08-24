from api.routes.hello import router as hello_router
from api.routes.report import router as report_router
from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="ReportQueue API",
    )
    app.include_router(hello_router)
    app.include_router(report_router)
    return app
