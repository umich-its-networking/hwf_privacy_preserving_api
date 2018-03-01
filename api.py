from flask import Flask, request, g
from flask_restful import Resource, Api

from privacy_preserving import PreserveCsv

app = Flask(__name__)
api = Api(app)

class Count(Resource):
    def get(self, query):
        count = g.private_source.count(query)
        return count

# @app.route("/count")
# def count():
#     query = request.args['query']
#     count = g.private_source.count(query)
#     return str(count)

api.add_resource(Count, '/count/<string:query>')

with app.app_context():
    g.private_source = PreserveCsv('./public_data/student-por.csv')
    app.run()
