import json


async def update_complete(data: dict):
    print(f"Updating the database with: {data}")
    with open(
        f"data/complete/{data['document_path'].split('/')[-1].split('.')[0]}.json",
        "w",
    ) as file:
        json.dump(data["extracted_terms"].model_dump(), file)


async def update_needs_review(data: dict):
    print("Sending trigger email to Human Reviewer")
    print(f"Updating the database with: {data}")
    with open(
        f"data/needs_review/{data['document_path'].split('/')[-1].split('.')[0]}.json",
        "w",
    ) as file:
        json.dump(data["extracted_terms"].model_dump(), file)
