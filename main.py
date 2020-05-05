from flask import Flask, render_template, url_for
import redis
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

red = redis.Redis()


class Temperature(Resource):
    def get(self):
        return {'temperature': red.get('temperature')}

api.add_resource(Temperature, '/temperature')


@app.route('/')
def hello_world():
    return render_template('index.html')



