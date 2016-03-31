__author__ = 'Nicolas Tomatis'
__version__ = "Version 1.2"
__copyright__ = "Copyright 2016, PydevAr"
__email__ = "pydev.ar@gmail.com"


RASPI = True  # True when used with a Raspberry, False for debug on PC.
CORRECT_VERTICAL_CAMERA = True  # Use this when camera is upside down only.
CORRECT_HORIZONTAL_CAMERA = True  # Use this when camera is showing mirrored image only.
RECORD_SECONDS = 30  # Number of seconds the video will last as maximum.

CENTER_RADIUS = 20  # Radius of circle that is detected
# The center of the light circle must be within this radius to appear as centered.

THRESHOLD = 50  # Threshold of brightness of lights to be detected (Range 0: darkest - 255 brightest)

