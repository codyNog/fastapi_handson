FROM python:3.9

RUN pip install --upgrade pip && pip --version
RUN pip install poetry && poetry --version
RUN poetry config virtualenvs.create false

WORKDIR /opt

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

COPY main.py /opt/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
