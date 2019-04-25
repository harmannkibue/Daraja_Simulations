from mpesa import app,api
from flask_restful import Resource
from flask import request, jsonify

class Test(Resource):
    def get(self):
        return {"harman": "ok"}

    def post(self):
        data = request.get_json()
        return data


api.add_resource(Test, "/")

if __name__ == "__main__":
    app.run(debug=True)