import smbus2
import bme280
import redis
import time

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)


r = redis.Redis(host='localhost', port=6379, db=0, protocol=3, password="password")
r.set('driver_bme280', 'on')

try:
  while True:
    # the sample method will take a single reading and return a
    # compensated_reading object
    data = bme280.sample(bus, address, calibration_params)

    # write to redis
    r.set('bme280:timestamp', str(data.timestamp))
    r.set('bme280:temperature', data.temperature)
    r.set('bme280:humidity', data.humidity)
    r.set('bme280:pressure', data.pressure)
    r.set('bme280:config:temperature_scale', 'celsius')

    print(data)
    time.sleep(2)

except Exception as e:
  print("Driver Exception")
  print(e)


r.set('driver_bme280', 'off')
