import sys
import time
from grove.gpio import GPIO
import redis
import configparser

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import switch

usleep = lambda x: time.sleep(x / 1000000.0)

_TIMEOUT1 = 1000
_TIMEOUT2 = 10000

upper_th = 100
lower_th = 70
wait_time = 10

class GroveUltrasonicRanger(object):
    def __init__(self, pin):
        self.dio = GPIO(pin)

    def _get_distance(self):
        self.dio.dir(GPIO.OUT)
        self.dio.write(0)
        usleep(2)
        self.dio.write(1)
        usleep(10)
        self.dio.write(0)

        self.dio.dir(GPIO.IN)

        t0 = time.time()
        count = 0
        while count < _TIMEOUT1:
            if self.dio.read():
                break
            count += 1
        if count >= _TIMEOUT1:
            return None

        t1 = time.time()
        count = 0
        while count < _TIMEOUT2:
            if not self.dio.read():
                break
            count += 1
        if count >= _TIMEOUT2:
            return None

        t2 = time.time()

        dt = int((t1 - t0) * 1000000)
        if dt > 530:
            return None

        distance = ((t2 - t1) * 1000000 / 29 / 2)    # cm

        return distance

    def get_distance(self):
        while True:
            dist = self._get_distance()
            if dist:
                return dist


Grove = GroveUltrasonicRanger


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    pin = int(config['DEFAULT']['ultrasonic_sensor_pin'])
    sonar = GroveUltrasonicRanger(pin)
    red = redis.Redis()
    sw = switch.Switch(int(config['DEFAULT']['switch3_pin']))
    print('Detecting distance...')
    i = 0
    state = 1
    while True:
        dist = sonar.get_distance()
        if state == 1:
            if dist < lower_th:
                state = 2
                red.mset({'presence': 1})
                sw.set_state(1)
                i = 0
        else:
            if dist > upper_th:
                i = i + 1
                if i > wait_time:
                    state = 1
                    red.mset({'presence': 0})
                    sw.set_state(0)
        time.sleep(1)

if __name__ == '__main__':
    main()
