from flask import Flask, request
from dotenv import dotenv_values
import mysql.connector

config = dotenv_values(".env")
connection_params = {
  'host': config['DB_HOST'],
  'user': config['DB_USER'],
  'password': config['DB_PASS'],
  'database': config['DB_NAME']
}
db = mysql.connector.connect(**connection_params)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return { "message": "Hello World" }

@app.route("/api/tasks", methods=["POST"])
def create_task():
    error = None
    query = "INSERT INTO `task` (`label`) VALUES (%s)"
    params = (request.form['label'],)
    with db.cursor() as c:
        try:
          c.execute(query, params)
          db.commit()
        except mysql.connector.errors.ProgrammingError as err:
          print(err)
          return { "status": "err" }
    return { "status": "ok" }

