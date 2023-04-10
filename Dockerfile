FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

ARG DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

COPY . /app

EXPOSE 7200

CMD ["python","main.py"]