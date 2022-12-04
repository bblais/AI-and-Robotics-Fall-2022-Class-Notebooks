from Robot373 import *

def take_picture(fname):
    print(r"""--- Opening /dev/video0...
Trying source module v4l2...
/dev/video0 opened.
No input was specified, using the first.
Setting Brightness to 255 (100%%).
Adjusting resolution from 1600x900 to 1600x896.
--- Capturing frame...
Captured frame in 0.00 seconds.
--- Processing captured image...
Disabling banner.
Writing JPEG image to '%s'.
    """ % fname)


def move_forward(distance):
    print("forward ",distance)
    
def move_backward(distance):
    print("backward ",distance)    
    
def turn_robot_left_90():
    print("left 90")
    
def turn_robot_right_90():
    print("right 90")    
    
def turn_robot_left_45():
    print("left 45")    
    
def turn_robot_right_45():
    print("right 45")     
    
def arm_up():
    print("arm up")
def arm_down():
    print("arm down")