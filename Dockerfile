FROM ubuntu:18.04
COPY ./S3Sync/ /app
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip
RUN python3 -m pip install --user boto3
CMD python3 /app/main.py