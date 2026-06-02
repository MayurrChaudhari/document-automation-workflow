from dotenv import load_dotenv
from fastapi import BackgroundTasks, UploadFile
from langchain_core.runnables import RunnableConfig
from pydantic import UUID4

from src.workflow.graph import graph

load_dotenv()


async def extract_contract(file: UploadFile):
    print("Saving the file ...")

    contents = await file.read()

    # Save the file locally
    with open(f"data/{file.filename}", "wb") as f:
        f.write(contents)

    print("Saved the file")
    correlation_id = UUID4
    config: RunnableConfig = {"configurable": {"thread_id": f"{correlation_id}"}}

    print("Invoking the graph...")

    BackgroundTasks.add_task(
        await graph.ainvoke(
            {
                "document_path": f"data/{file.filename}",
                "correlation_id": correlation_id,
                "transitions": ["start"],
            },
            config,
        )
    )
    print("Invoked the graph...")

    return {"success": "Task Triggered Successfully!"}
