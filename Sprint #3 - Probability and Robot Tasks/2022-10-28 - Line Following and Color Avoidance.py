#!/usr/bin/env python
# coding: utf-8

# Caveat -- haven't run this on the robot.  This first bit is shared between the various tasks.

# In[ ]:


from Robot373 import *

# initialize the sensors and motors
touch,color=Sensors("touch","color",None,None)  # color on sensor port S2
left,right=Motors("ab")


def wait_for_click():
    # do nothing until the touch sensor is pressed
    while not touch.value:
        Wait(0.01)

    # do nothing until the touch sensor is released
    while touch.value:
        Wait(0.01)

        
def calibrate():
    # calibrate    
    print("Place the color sensor on the white part of the line and click the touch sensor.")
    wait_for_click(touch)
    r1,g1,b1,something=color_sensor.value
    print("Place the color sensor on the black part of the line and click the touch sensor.")
    wait_for_click(touch)
    r2,g2,b2,something=color_sensor.value
    print("Place the robot where you want it to start and click the touch sensor.")
    wait_for_click(touch)

    white=[r1,g1,b1]
    black=[r2,g2,b2]
    
    return white,black
    
    
def forward(power=50):
    left.power=power
    right.power=power
    
    
def backward(power=50):
    left.power=-power
    right.power=-power

def degrees(position):
    return position*1.0  # not sure of the conversion factor here -- is it 1?

def turn_right(degrees):
    left.reset_position()
    
    left.power=50
    right.power=-50

    axis_length_cm=6
    pi=3.14159
    distance_needed=(axis_length_cm/2)*2*pi/360*degrees  # need a quarter turn of the robot

    try:
        while distance_traveled(left.position)<distance_needed:
            print("[turning right] distance traveled so far:",distance_traveled(left.position))
            Wait(0.01)
    except KeyboardInterrupt:
        pass
    
    left.power=0
    right.power=0
    
def turn_left(degrees):
    right.reset_position()
    
    left.power=-50
    right.power=50

    axis_length_cm=6
    pi=3.14159
    distance_needed=(axis_length_cm/2)*2*pi/360*degrees  # need a quarter turn of the robot

    try:
        while distance_traveled(right.position)<distance_needed:
            print("[turning right] distance traveled so far:",distance_traveled(right.position))
            Wait(0.01)
    except KeyboardInterrupt:
        pass
    
    left.power=0
    right.power=0
    


# Avoiding black

# In[ ]:


try:
    
    white,black=calibrate()
    
    
    while True:
        forward()
        
        r,g,b,something=color_sensor.value
        Wait(0.05)
        
        if closest_color(r,g,b,
                         white=white,
                         black=black,
                        )=="black":
            backward()
            Wait(1)
            turn_right(10)
            
except KeyboardInterrupt:
    pass

Shutdown()


# follow the line

# In[ ]:


try:
    
    white,black=calibrate()
    
    
    while True:
        forward()
        
        r,g,b,something=color_sensor.value
        Wait(0.05)
        
        if closest_color(r,g,b,
                         white=white,
                         black=black,
                        )=="white":  # went off of the line
            
            # look for the line
            while True:
                step=5
                
                if step>0:
                    turn_right(step)
                else:
                    turn_left(-step)
                    
                r,g,b,something=color_sensor.value

                if closest_color(r,g,b,
                             white=white,
                             black=black,
                            )=="black":
                    break  # found the line!
            
                # didn't find the line, so reverse direction and look again
                if step>0:
                    step=-step*2-5
                else:
                    step=-step*2+5
                    
            
except KeyboardInterrupt:
    pass

Shutdown()

