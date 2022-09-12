#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from mplturtle import *


# In[3]:


reset()
forward(50)
right(90)
forward(50)


# In[5]:


animate()


# ## Drawing a square

# In[ ]:


reset()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)


# In[7]:


reset()
for i in range(4):
    forward(50)
    right(90)


# ## square 100x100

# In[9]:


reset()
forward(110)
right(90)
forward(110)
right(90)
forward(110)
right(110)
forward(50)
right(90)


# In[11]:


size=10

reset()
forward(size)
right(90)
forward(size)
right(90)
forward(size)
right(90)
forward(size)
right(90)


# In[14]:


def square(size):
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)    


# In[15]:


reset()
square(40)


# In[16]:


def triangle():
    left(56)
    forward(50)
    right(124)
    forward(50)


# In[17]:


reset()
square(40)
triangle()


# In[18]:


def house():
    square(40)
    triangle()    


# In[20]:


reset()
house()


# In[21]:


animate()


# In[22]:


reset()
house()

forward(50)

house()


# In[24]:


reset()
house()

penup()
forward(50)
pendown()

pencolor("red")
house()


# In[ ]:




