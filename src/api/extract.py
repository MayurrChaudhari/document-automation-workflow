from fastapi import APIRouter, UploadFile

from src.services.extract import extract_contract

router = APIRouter()


@router.post("/extract_contract", tags=["extract"])
async def extract_contract_endpoint(file: UploadFile):
    try:
        await extract_contract(file)
    except Exception as e:
        RuntimeError(f"An Unexpected error occured: {e}")
