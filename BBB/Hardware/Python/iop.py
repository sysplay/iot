def analog_read(i):
	"Reads the ith analog input"
	try:
		f = open("/sys/bus/iio/devices/iio:device0/in_voltage" + str(i) + "_raw")
		return int(f.read())
	except:
		print("Analog input read failed.")
		return 0

def gpio_dir_set(i, dir):
	'Sets the dir ("in" | "out") for the ith gpio'
	try:
		f = open("/sys/class/gpio/gpio" + str(i) + "/direction", "w")
		f.write(dir)
		return
	except:
		print("GPIO direction set failed.")
		return

def gpio_read(i):
	"Reads the ith gpio"
	try:
		f = open("/sys/class/gpio/gpio" + str(i) + "/value")
		return int(f.read())
	except:
		print("GPIO read failed.")
		return 0

def gpio_write(i, val):
	"Write val into the ith gpio"
	try:
		f = open("/sys/class/gpio/gpio" + str(i) + "/value", "w")
		f.write(str(val))
		return
	except:
		print("GPIO write failed.")
		return

def led_set(i, val):
	"Set val into the ith led"
	try:
		print(i, val)
		f = open("/sys/class/leds/beaglebone:green:usr" + str(i) + "/brightness" , "w")
		f.write(str(val))
		return
	except:
		print("LED set failed.")
		return
