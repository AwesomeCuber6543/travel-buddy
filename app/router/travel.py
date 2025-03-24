from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(prefix="/travel")

router.post("/test")

