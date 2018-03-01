from flask import Flask, request, g
from privacy_preserving import PreserveCsv

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/count")
def count():
    query = request.args['query']
    count = g.private_source.count(query)
    return str(count)

with app.app_context():
    g.private_source = PreserveCsv('./public_data/student-por.csv')
    app.run()
