from fastapi import APIRouter
from schemas.hello_schema import HelloSchema

router = APIRouter(tags=["Health"], prefix="/health")


@router.get("/", response_model=HelloSchema)
async def getHello(text: str) -> str:
    return {"message": text}
