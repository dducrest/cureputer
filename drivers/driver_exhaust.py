
# PIN - GPIO18(PIN 12) on/off control to the Mosfet
# CHECK_KEY - the Redis key used that determines the ON/OFF state
# RANGE_ON_LOW/HIGH - 
PIN = 12
CHECK_KEY = "bme280:humidity"
RANGE_ON_LOW = 70
RANGE_ON_HIGH = 100

import RPi.GPIO as GPIO
import redis
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

r = redis.Redis(host='localhost', port=6379, db=0, protocol=3, password="password")

# TEST FAN on start
print("TEST EXHAUST FAN - START")
GPIO.output(PIN, GPIO.HIGH)
time.sleep(5)
GPIO.output(PIN, GPIO.LOW)
print("TEST EXHAUST FAN - DONE")

enable_exhaust = False
r.set("exhaust:on", str(enable_exhaust))

try:
  while True:
    value = float(r.get(CHECK_KEY))
    check = RANGE_ON_LOW <= value and value <= RANGE_ON_HIGH
    if check != enable_exhaust:
      enable_exhaust = check
      r.set("exhaust:on", str(enable_exhaust))
      GPIO.output(PIN, enable_exhaust)
    
    time.sleep(30)
except Exception as e:
  print('Driver Exhaust exception')
  print(e)


GPIO.output(PIN, GPIO.LOW)
