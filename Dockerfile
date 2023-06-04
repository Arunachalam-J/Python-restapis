FROM python:3.12.0b1-alpine3.18
USER root
COPY ./pyrestapis 
ENV FLASK_APP=./app/app.py
RUN groupadd -g svc && useradd -u 1001 -g svc svc
WORKDIR /home/svc
COPY . /app
USER 1001
RUN pip3 install --no-cache -r requirements.txt 
EXPOSE 8080
ENTRYPOINT ["flask","run","port=8080"]