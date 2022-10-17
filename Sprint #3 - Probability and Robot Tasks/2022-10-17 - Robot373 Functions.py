#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Robot373 import *


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


# In[ ]:





# The `Shutdown` command should be run only at the end of your script.  It disconnects the sensors, powers down motors, etc...

# In[ ]:


Shutdown()


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
# - "us": ![image.png](attachment:9978ae50-107e-4fe9-8f6e-1c0007c0aa35.png)
# - "color": ![image.png](attachment:8f3dc623-7598-4c5d-aaa0-f2bdb7d108a6.png)
# - "ir":  ![image.png](attachment:6f4e3abe-c478-4cf9-a17c-cd423ec45d1f.png)
# - "gyro": ![image.png](attachment:a9058d16-7342-4089-9c95-13e5bc4839ee.png)

# In[ ]:




