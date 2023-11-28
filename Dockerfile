FROM python:3.10

RUN mkdir /app
WORKDIR /app

ADD ./app/app.py .
ADD .env .
ADD requirements.txt .

RUN pip install --upgrade pip --no-cache-dir -r requirements.txt

EXPOSE 7860

CMD [ "python3", "app.py"]