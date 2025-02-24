FROM python:3.8-slim
WORKDIR /app
COPY chall.py .
RUN pip install pymodbus
EXPOSE 502
CMD ["python3", "chall.py"]