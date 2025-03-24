from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(prefix="/travel")

@router.get("/test")
def test():
    return {"MESSAGE":"IN TRAVEL TEST"}
