# indexor AI RAG Agent — Phase 1

## Quickstart

1. Create virtualenv and install deps:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
Copy .env (example provided) and edit:



For Phase 1 you may leave SOURCE_SYSTEM, OPENROUTER_KEY empty

Run the server:

bash
Copy code
uvicorn app.main:app --reload
http://127.0.0.1:8000/docs 

 run:
/api/v1/health/

/api/v1/status/

you will be having try it out tap on that and then 
execute 

for 
/api/v1/status/

enetr the key : changeme123
this is for testing purpose as we have set these key 
