from flask import Flask, redirect, request
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

    def __init__(self, csv_file):
        self._data = Preserve(pandas.read_csv(csv_file))

    @swagger.operation(
        dataType="object",
        parameters=[
            {
              "name": "query",
              "description": "DataFrame query by which to return a count.",
              "required": True,
              "allowMultiple": False,
              "dataType": "string",
              "paramType": "query",
            }
          ],
        )
    def get(self):
        return {
            'count': self._data.count(request.args.get('query')),
        }

    @swagger.operation(
        dataType="object",
        )
    def options(self):
        return self._data.attributes()


api.add_resource(Count, '/student/count/',
                 resource_class_args=('./public_data/student-por.csv',))

if __name__ == "__main__":
    app.run()
