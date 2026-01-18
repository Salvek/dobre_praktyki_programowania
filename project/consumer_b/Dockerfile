# Python 3.11 slim
FROM python:3.11-slim

# Instalacja wszystkich zależności systemowych dla OpenCV
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libx11-6 \
    libxcb1 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Katalog roboczy
WORKDIR /app

# Zainstaluj zależności Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj kod aplikacji
COPY . .

# Komenda startowa konsumenta
CMD ["python", "-m", "app.consumer"]

