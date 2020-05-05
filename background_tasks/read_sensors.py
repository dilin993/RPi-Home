import sys
import time
from grove.factory import Factory
import redis

INTERVAL=300  # 5 min

def main():
    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.ADC)
    pin = sh.argv2pin()
    red = redis.Redis()

    sensor = Factory.getTemper("NTC-ADC", pin)
    
    while True:
        temp = float(sensor.temperature)
        red.mset({'temperature': round(temp)})
        time.sleep(INTERVAL)


if __name__ == '__main__':
    main()
