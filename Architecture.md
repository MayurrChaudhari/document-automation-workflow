# Architecture

## LangGraph for Orchestration

1. Receive Doc
2. Read Doc
3. Extract Data
   1. Contract Type
   2. Effective Date
   3. Parties Involved
   4. Term Duration
   5. Governing Law
4. Evaluate / Confidence check
   1. heuristics: validate (ContractKeyTermsExtraction.model_validate(response.__dict__))
   2. can be llm-as-a-judge
5. Route
   1. complete
   2. need review
6. Persist
   1. JSON files

## Architecture plan that I couldn't complete because of time contraint

1. I had planned to use PostgreSQL for the data persistant.
2. I had planned the use of Celery Tasks along with Redis.
3. I had planned returning correlation id in the extract end-point
4. I had planned providing another endpoint which would accepr the correlation id and would return the extarcted data.
