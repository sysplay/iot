import machine
import time
import math
def pulse(l, t):
    for i in range(20):
        print('dutycycle :',int(math.sin(i / 10 * math.pi) * 500 + 500), ( i / 10 * math.pi),math.sin(i / 10 * math.pi))
        l.duty(int(math.sin(i/10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

def main():
    led = machine.PWM(machine.Pin(2))
    for i in range(10):
        pulse(led, 200)

if __name__ == '__main__':
    main()

