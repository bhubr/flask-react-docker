FROM python:3-alpine
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY app.py /app/
RUN apk add curl
RUN curl -o /app/wait-for-it.sh https://github.com/vishnubob/wait-for-it/blob/master/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

CMD ["./wait-for-it.sh", "db:3306", "--", "flask", "run"]