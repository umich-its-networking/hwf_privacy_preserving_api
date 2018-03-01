from flask import Flask, request, g
from privacy_preserving import PreserveCsv

app = Flask(__name__)

with app.app_context():

    g["private_source"] = PreserveCsv('/Users/jlost/Projects/privascope/hwf_privacy_preserving_api/public_data/student-por.csv')

    @app.route("/")
    def hello():
        return "Hello World!"

    @app.route("/count")
    def count():
        query = request.args.get('query', '')
        return g.private_source.count(query)

if __name__ == "__main__":
    app.run()
