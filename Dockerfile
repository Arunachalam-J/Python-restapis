FROM python:3.12.0b1-alpine3.18
USER root 
ENV FLASK_APP=./app/app.py
RUN groupadd -g svc && useradd -u 1001 -g svc svc
WORKDIR /home/svc
USER 1001
COPY ./app ./app
RUN pip3 install --no-cache -r requirements.txt 
EXPOSE 8080
ENTRYPOINT ["flask","run","port=8080"]