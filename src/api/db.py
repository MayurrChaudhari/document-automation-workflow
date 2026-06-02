from fastapi import APIRouter

from src.services.db import update_complete, update_needs_review

router = APIRouter()


@router.post("/update_complete", tags=["db"])
async def update_complete_endpoint(data: dict):
    try:
        await update_complete(data)
    except Exception as e:
        RuntimeError(f"An Unexpected error occured: {e}")


@router.post("/update_needs_review", tags=["db"])
async def update_needs_review_endpoint(data: dict):
    try:
        await update_needs_review(data)
    except Exception as e:
        RuntimeError(f"An Unexpected error occured: {e}")
