FROM python:3.9-slim-buster

## cria o workdir
WORKDIR /app

## copia os arquivos do nosso diretório raiz pra dentro do workdir
COPY . .

## instala as dependencias da applicação que estão no arquivo reuirements.txt
RUN pip install -r requirements.txt

## comando que vai rodar a aplicação na porta 8080
ENTRYPOINT [ "streamlit", "run", "main.py", "--server.port=8080", "server.addres=0.0.0.0" ] 
