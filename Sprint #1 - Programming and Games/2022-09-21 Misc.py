#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


state=Board(3,3)


# In[3]:


state


# In[4]:


state[2]=3
state[1]=4


# In[5]:


state


# In[6]:


3 in state


# In[7]:


1 in state


# In[10]:


player=1
moves=[]

if player==1:
    for value in [1,3,5,7,9]:
        if not value in state:
            for location in range(9):
                if state[location]==0:
                    moves.append( [value,location])


# In[11]:


moves


# In[12]:


value=int(input("What value will you play?"))
location=int(input("What location to play?"))
move=[value,location]


# In[13]:


move


# In[ ]:




