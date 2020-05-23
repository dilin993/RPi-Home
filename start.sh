#!/bin/bash

if [[ ! -e /tmp/read_sensors.py.pid ]]; then   # Check if the file already exists
    python background_tasks/read_sensors.py 0 &   #+and if so do not run another process.
    echo $! > /tmp/read_sensors.py.pid
else
    echo -n "ERROR: The process is already running with pid "
    cat /tmp/read_sensors.py.pid
    echo
fi



#FLASK_APP=main.py
#python -m flask run
