#!/usr/bin/env python
# coding: utf-8

# In[1]:


from breakthrough import *


# In[2]:


def get_move(state,player):
    if player==1:
        Q=LoadTable("Q1_breakthrough_table.json")
    else:
        Q=LoadTable("Q2_breakthrough_table.json")
        
    
    if state not in Q:
        return random_move(state,player)  # this is defined in my game functions import
    else:
        return top_choice(Q[state])
    
robot_agent=Agent(get_move)


# In[3]:


g=Game()  
g.run(robot_agent,human_agent)


# In[ ]:




