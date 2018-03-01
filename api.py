from flask import Flask, request, g, redirect
from flask_restful import Resource, Api
from flask_restful_swagger import swagger

import pandas
from privacy_preserving import Preserve

app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.1', api_spec_url='/spec')

@app.route('/')
def home():
    return redirect("/spec.html")

class Count(Resource):
    @swagger.operation(
        dataType="number",
        parameters=[
            {
              "name": "query",
              "description": "DataFrame query by which to return a count.",
              "required": True,
              "allowMultiple": False,
              "dataType": "string",
              "paramType": "path",
            }
          ],
        )
    def get(self, query):
        source = Preserve(pandas.read_csv('./public_data/student-por.csv'))
        count = source.count(query)
        return count

api.add_resource(Count, '/count/<string:query>')


if __name__ == "__main__":
    app.run()
