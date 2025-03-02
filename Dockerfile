# Use a imagem base do Python
FROM python:3-bookworm
RUN apt update && apt install git -y
RUN pip3 install tiktok_downloader
EXPOSE 80
# Especifique o comando a ser executado quando o contêiner for iniciado
CMD [ "python3", "-m", "tiktok_downloader", "--host=0.0.0.0", "--port=80", "--server" ]
