# How to run

- Start Docker engine.
- Setup .env file like attached in the same email
  - you can use the openai api key provided, I will be deactivating it later
  - use your own langsmith api key
- and run
  - docker compose build && docker compose up
- Head to:
  - <http://0.0.0.0:8000/docs>
  - use the "/extract_contract" endpoint.
  - you will get the extracted data results on local machine inside "data" folder.
