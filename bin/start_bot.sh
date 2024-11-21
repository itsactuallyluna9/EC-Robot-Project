#!/bin/bash

set -o errexit
#set -x

cd /home/c4/EC-Robot-Project

# do we have internet?
function checkInternet {
    curl -s --head  --request GET https://www.google.com | grep "200" > /dev/null
}

# wait for internet
while ! checkInternet; do
    sleep 5
done

git pull

# sudo python3 -m pip install -e .
# this takes a while to run. TODO: FIX.

sudo /home/c4/EC-Robot-Project/venv/bin/python3 -m robot_project

exit 0
