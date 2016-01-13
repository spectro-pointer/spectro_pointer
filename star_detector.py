__author__ = 'Nicolas Tomatis'
__version__ = "Version 1.0"
__copyright__ = "Copyright 2015, PydevAr"
__email__ = "pydev.ar@gmail.com"

from tracker_lib import *


# Test
def main():
    set_up_leds()
    camera_loop()

    # when code ends, the GPIO is freed...
    GPIO.cleanup()
    print "The program ended successfully."


if __name__ == "__main__":
    main()
