from gpiozerorpi import GPOut, GPIn
from signal import pause

GPOutPin = GPOut(17)
GPInPin = GPIn(3)

GPInPin.when_pressed = GPOutPin.high
GPInPin.when_released = GPOutPin.low

pause()