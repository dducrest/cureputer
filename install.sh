#!/usr/bin/bash

sudo cp ./services/driver_bme280.service /etc/systemd/system
sudo cp ./services/driver_exhaust.service /etc/systemd/system

sudo systemctl daemon-reload

sudo systemctl enable driver_bme280.service
sudo systemctl enable driver_exhaust.service

sudo systemctl restart driver_bme280.service
sudo systemctl restart driver_exhaust.service

sudo systemctl status driver_bme280.service
sudo systemctl status driver_exhaust.service

