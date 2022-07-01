FROM python:3.10.5-buster

RUN mkdir -p /app
COPY . main.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora
EXPOSE 8282
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]