FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./ml-project/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./ml-project/app /app/app


EXPOSE ${PORT}