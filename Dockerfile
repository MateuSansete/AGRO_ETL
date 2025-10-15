# Usa uma imagem base Python com Alpine 
FROM python:3.9-slim-buster

# Configura o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do projeto
COPY . .

# Comando de entrada padrão (será sobrescrito pelo docker-compose)
CMD ["python", "etl/etl_pipeline.py"]