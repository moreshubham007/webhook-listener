FROM python:3.8
WORKDIR /app
COPY .  .
RUN pip install -r requirements.txt
EXPOSE 8181
CMD ["python3","server.py"]
