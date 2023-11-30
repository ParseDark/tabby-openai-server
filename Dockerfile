FROM python:3.11-slim

WORKDIR /code

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD exec python main.py --host 0.0.0.0 --port 8080
