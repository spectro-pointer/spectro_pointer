__author__ = 'Nicolas Tomatis'
__version__ = "Version 1.2"
__copyright__ = "Copyright 2016, PydevAr"
__email__ = "pydev.ar@gmail.com"


# ------------------------- CAMERA CONFIGURATION ------------------------------ #
USE_RASPBERRY = True
# True when used with a Raspberry, False for debug on PC.

CORRECT_VERTICAL_CAMERA = True
# Use this when camera is upside down only.

CORRECT_HORIZONTAL_CAMERA = True
# Use this when camera is showing mirrored image only.

# ------------------------- IMAGE CONFIGURATION ------------------------------- #
CENTER_RADIUS = 20
# Radius of circle that is detected.
# The center of the light circle must be within this radius to appear as centered.

THRESHOLD = 50
# Threshold of brightness of lights to be detected (Range 0: darkest - 255 brightest)

# ---------------------------- OUTPUT FILES --------------------------------- #
ENABLE_PHOTO = True
# When set to True, photos are taken when the object appears, and is centered.

ENABLE_VIDEO = True
# When set to True, a video is taken starting when the object appears and finishes when the object
# is centered. The video takes a limited times of seconds, if that time passes, the video is cut.

RECORD_SECONDS = 30  # Number of seconds the video will last as maximum.
