from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Factory(Resource):
    
    def get(self):
        return {
            'cars': ['Audi', 'BMW', 'Mercedes',]
        }

api.add_resource(Factory, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)


