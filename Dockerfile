FROM python:3.7
MAINTAINER saphi070@gmail.com

WORKDIR /app/
COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY * /app/

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]