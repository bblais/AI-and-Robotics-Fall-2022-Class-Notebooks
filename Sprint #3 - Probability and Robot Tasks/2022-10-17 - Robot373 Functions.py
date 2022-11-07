#!/usr/bin/env python
# coding: utf-8

# - The Robot373 library is at https://github.com/bblais/Robot373
# - Download and Install it with:
# 
# `pip install "git+https://github.com/bblais/Robot373" --upgrade`

# In[2]:


from Robot373 import *


# # Motors

# The `Motors` function defines where the motors are connected.  In this example, we have a motor on port A which we will label `left` and one on port B which we label as `right`

# In[ ]:


left,right=Motors("ab")


# if you have your left motor on port C and right motor on B, you'd use

# In[ ]:


left,right=Motors("cb")


# You can set the power on a motor to between -100 and 100, for full power backward to full power forward using  `motorname.power=value`

# In[ ]:


left.power=+50
right.power=-50


# The `Wait` command doesn't do anything -- it sits at that point for the number of seconds.  Recall that motor commands like `left.power=50` is like light switch and won't change until another `left.power` assignment.  
# 
# The following example runs the left motor for 5 seconds.

# In[ ]:


left.power=50
Wait(5)  # wait for 5 seconds
left.power=0


# You can also read the current position of a robot motor (related to the angle it has turned) by using the `position` attribute, like

# In[ ]:


left.position


# The units for this position are somewhat arbitrary, so you'll have to figure out how it relates to angle turned.  You can reset this with the `reset_position` function.

# In[ ]:


left.reset_position()


# In[ ]:





# The `Shutdown` command should be run only at the end of your script.  It disconnects the sensors, powers down motors, etc...

# In[ ]:


Shutdown()


# # Sensors

# The `Sensors` function defines where the sensors are connected and what type they are.  Use `None` if there is nothing connected.
# 
# This example has the ultrasonic distance sensor (i.e. eyes) connected on port S3 and a touch sensor connected on port S4.  There is nothing connected to ports S1 and S2.

# In[ ]:


eyes,touch=Sensors(None,None,"us","touch")


# To get the value of a sensor, use `sensorname.value`.  Depending on the type of sensor, you may get a single number (e.g. ultrasonic and touch) or multiple numbers (e.g. color).  The number means different things depending on the sensor.
# 
# Types of sensors:
# 
# - "touch":  ![image.png](attachment:4f257ea6-2c31-4c76-bf69-adb2a65b8a16.png)
# - "us" or "ultrasonic": ![image.png](attachment:9978ae50-107e-4fe9-8f6e-1c0007c0aa35.png)
# - "color": ![image.png](attachment:8f3dc623-7598-4c5d-aaa0-f2bdb7d108a6.png)
# - "ir":  ![image.png](attachment:6f4e3abe-c478-4cf9-a17c-cd423ec45d1f.png)
# - "gyro": ![image.png](attachment:a9058d16-7342-4089-9c95-13e5bc4839ee.png)

# ### To test a sensor, set up a loop and print the value

# The following will print out the value of the color sensor every 1/20 of a second until you hit `CTRL-C` (i.e. `KeyboardInterrupt`) to stop the program.

# In[ ]:


from Robot373 import *

color_sensor=Sensors(None,"color",None,None)

try:
    while True:
        color=color_sensor.value
        print(color)
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# ### TypeError: NoneType object....

# It takes a little bit for sensors to give reasonable values.  Until they warm up, they return `None` for their value.  To solve it, you need to wait until the sensor starts returning reasonable things.
# 
# Method #1:  Put a `Wait` command.

# In[ ]:


from Robot373 import *

color_sensor=Sensors(None,"color",None,None)
Wait(3)

try:
    while True:
        color=color_sensor.value
        print(color)
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# a better way is to check the sensor to be not None.

# In[ ]:


from Robot373 import *

color_sensor=Sensors(None,"color",None,None)

print("Waiting for sensor to warm up...")
while color_sensor.value is None:
    Wait(0.05)
print("done.")



try:
    while True:
        color=color_sensor.value
        print(color)
        Wait(0.05)
except KeyboardInterrupt:
    pass

Shutdown()


# ## Colors

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Timers
# 
# You can make a timer with the `Timer` object.  The `timer.value` returns the time in seconds since the timer was reset.  An example would be this, which prints out a value every 0.1 seconds for 5 seconds.

# In[ ]:


timer=Timer()
while timer.value<5:
    print(left.position,right.position)
    Wait(.1)


# ## Images

# In[ ]:


from Robot373 import *

take_picture("my cool pic.jpg")

print('Pausing for a few seconds for another image, but with viewing')
for i in range(5,0,-1):
    print(i)
    Wait(1)
    
take_picture("my cool pic2.jpg")


# In[ ]:





# # Programming pattern -- flags

# It is a common programming pattern to have a true/false (i.e. boolean) variable called a flag that keeps track of an event that toggles.  For example, if you want to have something happen when a button is pressed -- but don't want to do that thing while you're holding the button down, you can use a flag.   Here's an example which prints something when a button is pressed and then again when the button is released.

# In[ ]:


touch=Sensors("touch",None,None,None)

pressed=False

while True:
    if touch.value and not pressed:
        print("Button Pressed")
        pressed=True
    elif not touch.value and pressed:
        print("Button Released")
        pressed=False


# compare is with the same code without the flag, and you'll see the difference immediately.

# In[ ]:


while True:
    if touch.value:
        print("Button Pressed")
    elif not touch.value:
        print("Button Released")


# # Running on the robot

# - Edit the files on your robot
#     - VS Code with the Remote SSH Extension
#     - FileZilla or any other SSH/SFTP client
# - Run the files on your robot
# 
# ```
# glop-/Users/bblais-> ssh pi@10.2.2.32
# pi@10.2.2.32's password:
# Linux dex 4.19.66-v7+ #1253 SMP Thu Aug 15 11:49:46 BST 2019 armv7l
# 
# The programs included with the Debian GNU/Linux system are free software;
# the exact distribution terms for each program are described in the
# individual files in /usr/share/doc/*/copyright.
# 
# Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
# permitted by applicable law.
# Last login: Mon Oct 17 14:06:26 2022 from 10.100.52.148
# pi@dex:~ $ cd python
# pi@dex:~/python $ ls
# motorAB_test.py
# pi@dex:~/python $ python motorAB_test.py
# ```

# In[ ]:




