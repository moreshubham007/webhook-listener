FROM python:3.8-slim-buster
LABEL maintainer="shubhammore007@outlook.com"
WORKDIR /app
COPY ./source  .
RUN pip install -r requirements.txt
EXPOSE 8181
CMD ["python3","app.py"]
