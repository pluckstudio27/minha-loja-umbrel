# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de dependências e instale-as
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie todos os arquivos da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta que a aplicação vai usar
EXPOSE 8000

# Comando para iniciar a aplicação quando o contêiner for executado
CMD ["python", "app.py"]