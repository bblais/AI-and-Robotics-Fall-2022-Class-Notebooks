#!/usr/bin/env python
# coding: utf-8

# Write functions so that you can:
# 
# 

# These will be sketches of them.  I haven't debugged them, so there may even be typos!  :-)- use the ultrasonic sensor to give distances in meters or feet (whichever you’re more comfortable with)
# 

# - use the ultrasonic sensor to give distances in meters or feet (whichever you’re more comfortable with)
# 

# In[ ]:


from Robot373 import *

def distance_in_inches(distance_in_cm):
    return distance_in_cm/100*39


eyes,touch=Sensors(None,None,"us","touch")

try:
    while True:
        distance=eyes.value  # distance in cm
        print(distance_in_inches(distance))
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# - use the motor value to give degrees turned
# 

# In[ ]:


from Robot373 import *

def degrees(position):
    return position*1.0  # not sure of the conversion factor here -- is it 1?

left,right=Motors("ab")

try:
    while True:
        print(degrees(left.position))
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# - use the motor value to give distance traveled, given the wheel size

# In[ ]:


from Robot373 import *

def degrees(position):
    return position*1.0  # not sure of the conversion factor here -- is it 1?

def distance_traveled(position):
    wheel_diameter_cm=2
    pi=3.141592653589793235
    
    return pi*wheel_diameter_cm*degrees(position)/360

    
    

left,right=Motors("ab")

left.power(50)
right.power(50)



try:
    while True:
        print("distance traveled so far:",distance_traveled(left.position))
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# In[ ]:





# - given the axis size and wheel size, use the motor value to turn robot 90 degrees
# 

# In[ ]:


from Robot373 import *

def degrees(position):
    return position*1.0  # not sure of the conversion factor here -- is it 1?

def distance_traveled(position):
    wheel_diameter_cm=2
    pi=3.141592653589793235
    
    return pi*wheel_diameter_cm*degrees(position)/360

    
    

left,right=Motors("ab")

left.power(50)
right.power(-50)

axis_length_cm=6
distance_needed=(axis_length_cm/2)*2*pi/4  # need a quarter turn of the robot



try:
    while distance_traveled(left.position)<distance_needed:
        print("distance traveled so far:",distance_traveled(left.position))
        Wait(0.01)
except KeyboardInterrupt:
    pass

Shutdown()


# - use the color sensor to distinguish two colors (could be black and white, or any other pair of colors)

# In[ ]:


from Robot373 import *

color_sensor=Sensors("color",None)

try:
    while True:
        if not value:  # in case there is an illegal sensor value
            continue

        r,g,b,something=color_sensor.value
        print(r,g,b,something)
        print(closest_color(r,g,b,
                maroon=[128,0,0],
                gray=[128,128,128],
                white=[256,256,256],
                black=[0,0,0],
                ))
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# - use the touch sensor to do each of the following:
#     - do something if the sensor is pressed
#     - do something only if the sensor is pressed and then released
#     - do something if the sensor is “double clicked” within a reasonably short time period

# In[ ]:





# - go forward for 3 seconds if a button is **pressed**

# In[ ]:


from Robot373 import *

eyes,touch=Sensors(None,None,"us","touch")

left,right=Motors("ab")


# do nothing until the touch sensor is pressed
while not touch.value:
    Wait(0.01)

left.power(50)
right.power(50)

Wait(3)

Shutdown()


# - go forward for 3 seconds if a button is **pressed and released**

# In[ ]:


from Robot373 import *

eyes,touch=Sensors(None,None,"us","touch")

left,right=Motors("ab")


# do nothing until the touch sensor is pressed
while not touch.value:
    Wait(0.01)

# do nothing until the touch sensor is released
while touch.value:
    Wait(0.01)
    
    
left.power(50)
right.power(50)

Wait(3)

Shutdown()


# - go forward for 3 seconds if a button is **double-clicked**

# In[ ]:


from Robot373 import *

def wait_for_double_click(touch):
    
    double_click_time=0.5  # seconds
    timer=Timer()
    count=0
    stop=False
    while not stop:
        
        # do nothing until the touch sensor is pressed
        while not touch.value:
            Wait(0.01)

        # do nothing until the touch sensor is released
        while touch.value:
            Wait(0.01)
        
        count+=1

        if count>=2:  # double-click
            if timer.value>double_click_time:  # too long between "clicks":
                timer._reset()  # restart the timer at t=0
                count=0
        else:
            stop=True
        

eyes,touch=Sensors(None,None,"us","touch")

left,right=Motors("ab")

wait_for_double_click(touch)
    
    
left.power(50)
right.power(50)

Wait(3)

Shutdown()

