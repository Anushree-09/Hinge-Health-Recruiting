from fastapi import APIRouter, Response, status

router = APIRouter(prefix="/task", tags=["tasks"])

@router.post("/")
async def create_task():
    return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)

@router.get("/")
async def find_all():
    return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)

@router.patch("/{id}/share")
async def share(id: int):
    return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)

@router.put("/{id}")
async def update(id: int):
    return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)

@router.delete("/{id}")
async def remove(id: int):
    return Response(status_code=status.HTTP_501_NOT_IMPLEMENTED)
