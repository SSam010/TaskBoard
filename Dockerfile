FROM python:3.11.2
WORKDIR /usr/src/taskboard
COPY requirements.txt .
RUN pip3 install -r requirements.txt
