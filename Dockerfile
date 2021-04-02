FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR ./API /API


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD ["uvicorn", "API.api:app"]