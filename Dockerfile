FROM python:2.7
MAINTAINER saphi070@gmail.com

WORKDIR /app/
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY * /app/

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
