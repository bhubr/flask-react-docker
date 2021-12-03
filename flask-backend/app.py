from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import dotenv_values
import mysql.connector
import os

config = {
    **dotenv_values(".env"),
    **os.environ,
}

connection_params = {
    'host': config['DB_HOST'],
    'database': config['DB_NAME'],
    'user': config['DB_USER'],
    'password': config['DB_PASS'],
}

db = mysql.connector.connect(**connection_params)

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return {"message": "Hello World"}


@app.route("/api/tasks", methods=["GET", "POST"])
def tasks():
    error = None
    if request.method == 'POST':
        query = "INSERT INTO `task` (`label`) VALUES (%s)"
        label = request.form['label']
        params = (label,)
        with db.cursor() as c:
            try:
                c.execute(query, params)
                db.commit()
                id = c.lastrowid
                return {
                    "id": id,
                    "label": label
                }
            except mysql.connector.errors.ProgrammingError as err:
                print(err)
                return {"status": "err"}
    else:
        query = "SELECT * FROM `task`"
        with db.cursor() as c:
            try:
                c.execute(query)
                rv = c.fetchall()
                row_headers = [x[0] for x in c.description]
                json_data = []
                for result in rv:
                    json_data.append(dict(zip(row_headers, result)))
                return jsonify(json_data)
            except mysql.connector.errors.ProgrammingError as err:
                print(err)
                return {"status": "err"}
