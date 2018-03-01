from flask import Flask, request, g
import pandas
from privacy_preserving import Preserve

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
    g.private_source = Preserve(pandas.read_csv('./public_data/student-por.csv'))
    app.run()
