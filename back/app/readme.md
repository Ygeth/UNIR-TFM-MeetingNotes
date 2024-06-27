pip -m venv venv
venv\Scripts\activate
pip install fastapi python-multipart
pip install sqlalchemy

cd back
.\app\venv\Scripts\activate
fastapi dev ./app/src/main.py