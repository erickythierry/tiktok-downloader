# Dockerfile atualizado
FROM python:3-bookworm
RUN apt update && apt install git -y
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 80
CMD ["python3", "-m", "tiktok_downloader", "--host=0.0.0.0", "--port=80", "--server"]