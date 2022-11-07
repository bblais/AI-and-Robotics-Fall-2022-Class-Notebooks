#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def state_to_observation(state,player):
    deckk,hand1,hand2=state
    
    if player==1:
        observation=hand1,hand2[1:]  
        
    else:
        observation=hand2,hand1[1:]
        
    
    return observation

