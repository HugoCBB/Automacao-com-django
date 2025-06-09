# Define a versao da imagem
FROM python:3.13

# Diretorio atual dentro da imagem
WORKDIR /app-django

# Define a porta onde o container esta rodando dentro do docker
EXPOSE 8080

# Copia o conteudo do diretorio para o diretorio dentro da imagem
COPY . .

# Instala as dependencias do projeto
RUN pip install -r requirements.txt

# Roda o sistema
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
