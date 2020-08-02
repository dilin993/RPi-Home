import sys
import time
from grove.factory import Factory
import redis
import configparser

INTERVAL=300  # 5 min

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    pin = int(config['DEFAULT']['temp_sensor_pin'])
    red = redis.Redis()

    sensor = Factory.getTemper("NTC-ADC", pin)
    
    while True:
        temp = float(sensor.temperature)
        red.mset({'temperature': round(temp)})
        time.sleep(INTERVAL)


if __name__ == '__main__':
    main()
