from flask import Flask, render_template, url_for
import redis
from flask_restful import Resource, Api
import switch
import configparser


app = Flask(__name__)
api = Api(app)

red = redis.Redis()

# read config file
config = configparser.ConfigParser()
config.read('config.ini')
switches=[]
switches.append(switch.Switch(int(config['DEFAULT']['switch1_pin'])))
switches.append(switch.Switch(int(config['DEFAULT']['switch2_pin'])))



class Temperature(Resource):
    def get(self):
        return {'temperature': red.get('temperature')}
        
        
class SwitchOnOff(Resource):
    
    def put(self, sw_id):
        sw_id = int(sw_id)
        if switches[sw_id].get_state() == 0:
            switches[sw_id].set_state(1)
        else:
            switches[sw_id].set_state(0)
        return switches[sw_id].get_state()
        
class Presence(Resource):
    def get(self):
        return {'presence': red.get('presence')}
        

api.add_resource(Temperature, '/temperature')
api.add_resource(SwitchOnOff, '/switch/<sw_id>')
api.add_resource(Presence, '/presence')


@app.route('/')
def hello_world():
    return render_template('index.html',
    switches=[str(i) for i in range(len(switches))])



