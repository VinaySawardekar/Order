FROM python:3.9

WORKDIR /Order

COPY ./requirements.txt /Order/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Order/requirements.txt

COPY ./app /Order/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]