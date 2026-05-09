uv init
uv venv
.venv\Scripts\Activate.ps1
uv add -r requirements.txt
uvicorn app:app --reload

for langgraph studio
langgraph dev