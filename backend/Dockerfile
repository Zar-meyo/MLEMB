FROM python:3.12

WORKDIR /code


COPY requirements.txt /code/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/backend
COPY regression.joblib /code/regression.joblib

CMD ["fastapi", "run", "backend/backend.py", "--port", "80"]