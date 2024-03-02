FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app ./app
COPY config.py run.py gunicorn.conf.py ./

ENV FLASK_DEBUG=False
ENV FLASK_APP=run.py


EXPOSE 8080
CMD ["gunicorn", "--config", "gunicorn.conf.py", "run:app"]