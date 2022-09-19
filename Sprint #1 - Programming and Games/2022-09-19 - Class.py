#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(5):
    for j in range(6):
        print("i is ",i, "and j is ",j)


# In[2]:


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


# In[7]:


reset()
draw_row(8)

penup()

forward(100)
right(45)
forward(20)
right(30)
forward(50)


pendown()


draw_row(7)


# In[10]:


reset()
for i in [8,7,6,5,4]:
    draw_row(i)
    forward(100)
    print(i)


# In[ ]:




