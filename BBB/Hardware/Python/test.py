from iop import *

print("AIN0:", analog_read(0))
print("AIN1:", analog_read(1))
print("AIN2:", analog_read(2))
print("AIN3:", analog_read(3))
print("AIN4:", analog_read(4))
print("AIN5:", analog_read(5))
print("AIN6:", analog_read(6))

gpio_dir_set(50, "in")
print("GPIO50:", gpio_read(50))
gpio_dir_set(51, "out")
gpio_write(51, 1)
led_set(0, 1)
