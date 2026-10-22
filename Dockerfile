FROM python:3.12-alpine
WORKDIR /app
COPY service.py /app/app.py
EXPOSE 8000
CMD ["python", "-u", "app.py"]
