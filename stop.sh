#!/bin/bash

if [[ -e /tmp/read_sensors.py.pid ]]; then   # If the file do not exists, then the
    kill `cat /tmp/read_sensors.py.pid`      #+the process is not running. Useless
    rm /tmp/read_sensors.py.pid              #+trying to kill it.
else
    echo "read_sensors.py is not running"
fi


if [[ -e /tmp/rpi-home.pid ]]; then   # If the file do not exists, then the
    kill `cat /tmp/rpi-home.pid`      #+the process is not running. Useless
    rm /tmp/rpi-home.pid              #+trying to kill it.
else
    echo "read_sensors.py is not running"
fi

