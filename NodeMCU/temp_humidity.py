import dht
import machine
import utime

d = dht.DHT11(machine.Pin(4))
while True:
    d.measure()
    temp = d.temperature() # eg. 23 (°C)
    humid = d.humidity()    # eg. 41 (% RH)
    print('Temperature :',temp,'Humidity' , humid)
    utime.sleep(5)
