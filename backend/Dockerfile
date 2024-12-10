FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY train_model.py .
COPY app.py .

RUN python train_model.py

CMD ["python", "app.py"]
