FROM python:3.11-slim

WORKDIR /code

# Copia todo o código da aplicação para dentro do container
COPY ./app /code/app

# Instala as dependências
RUN pip install --upgrade pip
RUN pip install -r /code/app/requisitos.txt

# Garante que o pacote app será encontrado nos imports
ENV PYTHONPATH=/code

EXPOSE 8000

# Comando p/ iniciar o servidor FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]