import uvicorn
from fastapi import FastAPI

from .api import extract_router

app = FastAPI(
    title="Document Automation Management",
    description="An app to automate document data extraction.",
    version="0.1.0",
)

app.include_router(extract_router)


@app.get("/", tags=["heart beat"])
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
