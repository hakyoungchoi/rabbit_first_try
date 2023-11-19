from fastapi import APIRouter

router = APIRouter(dependencies=[])

@router.get("/my_stock")
async def get_my_stock() :
    return "rich rich man mans"