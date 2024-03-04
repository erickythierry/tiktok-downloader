# Use a imagem base do Python
FROM ubuntu:latest
RUN apt update && apt install git python3 python3-pip -y
RUN pip3 install tiktok_downloader
EXPOSE 80
# Especifique o comando a ser executado quando o contêiner for iniciado
CMD [ "python3", "-m", "tiktok_downloader", "--host=0.0.0.0", "--port=80", "--server" ]
