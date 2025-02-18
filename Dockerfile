FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install procps package to get the top command
RUN apt-get update && apt-get install -y procps

COPY . .

CMD ["python", "app.py"]
