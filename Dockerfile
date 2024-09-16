
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY web_scraper.py web_scraper.py

CMD ["python", "web_scraper.py"]
