FROM python:latest
WORKDIR /app
COPY . .
COPY Pipfile ./
RUN pip install pipenv
RUN pipenv install
EXPOSE 8080
CMD ["pipenv", "run", "python", "app.py"]