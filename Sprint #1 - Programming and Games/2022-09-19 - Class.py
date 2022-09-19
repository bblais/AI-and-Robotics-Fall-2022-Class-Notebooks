#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(5):
    for j in range(6):
        print("i is ",i, "and j is ",j)


# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from mplturtle import *


# In[3]:


def square(size):
    for i in range(4):
        forward(size)
        right(90)
        
def draw_row(N):
    for i in range(N):
        square(10)
        forward(10)


# In[11]:


reset()
draw_row(8)

penup()

forward(100)
right(45)
forward(20)
right(30)
forward(50)


pendown()


pencolor("red")
draw_row(7)


# In[10]:


reset()
for i in [8,7,6,5,4]:
    draw_row(i)
    forward(100)
    print(i)


# In[13]:


print("start")
for i in range(4):
    print("here",i)
    print("another")
    
print("end")


# In[14]:


c=6
def myfunction():
    a=5
    print("bob")
    
    return 6
print("hello")


# In[15]:


myfunction()


# In[18]:


def myfunction():
    a=5
    print("bob")
    
    for j in range(10):
        print(j," ",end="")
    print("another")
    return 6


# In[19]:


myfunction()


# In[2]:


reset()
forward(100)
backward(100)
left(20)
forward(100)
backward(100)
left(20)
forward(100)
backward(100)
left(20)
forward(100)
backward(100)
left(20)


# In[9]:


color1="blue"
color2="red"

reset((8,8))
for i in range(10):
    
    pencolor(color1)
    square(5)
    
    forward(6)
    
    color1,color2=color2,color1


# In[ ]:




