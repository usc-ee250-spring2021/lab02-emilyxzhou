""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
import grove_rgb_lcd


ULTRASONIC_PORT = 4  # D4
POTENTIOMETER_PORT = 0  # A0


def poll_sensors():
    ult_value = round(grovepi.ultrasonicRead(ULTRASONIC_PORT))
    threshold = round(grovepi.analogRead(POTENTIOMETER_PORT)*517/1023)
    return ult_value, threshold


def update_line_1(threshold, ult_value):
    line1 = "{}cm".format(threshold)

    if ult_value <= threshold:
        line1 += " OBJ PRES"
        grove_rgb_lcd.setRGB(255, 0, 0)
    else:
        grove_rgb_lcd.setRGB(0, 255, 0)

    grove_rgb_lcd.setText_norefresh("{}".format(line1))


def update_line_2(ult_value):
    line2 = "{}cm".format(ult_value)
    grove_rgb_lcd.setText_norefresh("\n{}".format(line2))

        
if __name__ == '__main__':

    ult_value, threshold = poll_sensors()
    update_line_1(threshold, ult_value)
    update_line_2(ult_value)

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        new_ult_value, new_threshold = poll_sensors()
        update_line_1(new_threshold, new_ult_value)
        update_line_2(new_ult_value)
