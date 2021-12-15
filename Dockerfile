# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8.0 AS builder

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app


# Install pip requirements
COPY requirements.txt .
RUN  python -m pip install --no-cache-dir -r requirements.txt 


FROM python:3.8.0
WORKDIR /app
COPY --from=builder /app /app
COPY app.py .


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "--access-logfile", "-",  "main:app"]
