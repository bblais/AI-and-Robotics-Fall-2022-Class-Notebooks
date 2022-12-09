#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


T=LoadTable("mcts_data_TTT.json")


# In[9]:


S=Board(3,3)
S.board[-1]=1


# In[10]:


float(T[(S,1)]['wins'])/T[(S,1)]['plays']


# In[8]:


T


# In[ ]:




