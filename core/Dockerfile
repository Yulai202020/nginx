### INIT
FROM python:3.8-slim
WORKDIR /urs/src/app

### Install requirements
RUN apt update && apt install -y dnsutils net-tools inetutils-ping curl

### Copy Project
COPY . .

### Install Requirements For Project
RUN pip install --upgrade pip && pip install -r requirements.txt

### Run Project
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]