import time
import board
import adafruit_dht
import psutil
# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
sensor = adafruit_dht.DHT11(board.D4)
while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        print("humidity: {}%".format(humidity))
        if humidity < 40:
            print ("terlalu kering")
        elif humidity > 60:
            print ("lembab")
        else:
            print ("kelembapan normal")
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(2.0)