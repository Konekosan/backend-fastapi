python -m venv env
env\Scripts\activate #Win
source venv/bin/activate #WSL/Linux
uvicorn app.main:app --reload

