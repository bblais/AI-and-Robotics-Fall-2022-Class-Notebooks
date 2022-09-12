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


# In[12]:


def square(size):
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)    


# In[13]:


reset()
square(40)


# In[ ]:




