#!/bin/bash

if [[ ! -e /tmp/read_temp_sensor.py.pid ]]; then   # Check if the file already exists
    python background_tasks/read_temp_sensor.py 0 &   #+and if so do not run another process.
    echo $! > /tmp/read_temp_sensor.py.pid
else
    echo -n "ERROR: The process is already running with pid "
    cat /tmp/read_temp_sensor.py.pid
    echo
fi

if [[ ! -e /tmp/read_ultrasonic_sensor.py.pid ]]; then   # Check if the file already exists
    python background_tasks/read_ultrasonic_sensor.py 0 &   #+and if so do not run another process.
    echo $! > /tmp/read_ultrasonic_sensor.py.pid
else
    echo -n "ERROR: The process is already running with pid "
    cat /tmp/read_ultrasonic_sensor.py.pid
    echo
fi



export FLASK_APP=main.py
#python -m flask run
if [[ ! -e /tmp/rpi-home.pid ]]; then   # Check if the file already exists
    python -m flask run --host=0.0.0.0 &   #+and if so do not run another process.
    echo $! > /tmp/rpi-home.pid
else
    echo -n "ERROR: The process is already running with pid "
    cat /tmp/rpi-home.pid
    echo
fi

