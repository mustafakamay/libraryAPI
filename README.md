# libraryAPI

This API built with FastAPI and used MongoDB,Redis,Celery

### Project Setup

``
virtualenv venv

venv/Scripts/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
``
or

``
docker-compose up --build -d
``

### Project Documents

``
http://127.0.0.1:8000/docs
``

### Test Data Create

``
-method: Post
http://127.0.0.1:8000/tests/add
``
### Celery worker
``
celery -A app.celery_worker worker
``
