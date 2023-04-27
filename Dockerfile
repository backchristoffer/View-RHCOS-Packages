FROM python:latest

WORKDIR /app

COPY Pipfile ./
RUN pip install pipenv
RUN pipenv install
EXPOSE 8080

COPY . .

CMD ["pipenv", "run", "python", "app.py"]