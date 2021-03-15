FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app/fastapi_skeleton /app/app
# COPY ./app/fastapi_skeleton/models /app/app/trained_models


EXPOSE 5340