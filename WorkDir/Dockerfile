FROM python:3.13.5

WORKDIR /app

COPY main.py .

RUN pip install psycopg2-binary

EXPOSE 5432

CMD ["python, "main.py""]
