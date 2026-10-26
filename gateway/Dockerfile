FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar primero los requirements para aprovechar la cache de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer el puerto donde correra FastAPI
EXPOSE 8000

# Comando para arrancar el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]