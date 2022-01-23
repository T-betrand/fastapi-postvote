FROM python:3.9

WORKDIR /pytut

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /pytut/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

#CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
