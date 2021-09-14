#!/usr/bin/bash

pip3 install notify-py

sudo rm -rf ~/.local/bin/ontime /opt/ontime
mv ./ontime /opt/
ln -s /opt/ontime/ontime.py ~/.local/bin/ontime

echo "installation done, enjoy"
