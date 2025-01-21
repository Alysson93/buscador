FROM python:3.12.1-slim

# Define o diretório de trabalho
WORKDIR /app/

# Copia o arquivo requirements.txt e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o container
COPY . .

# Define o comando de inicialização
CMD ["python", "main.py"]
