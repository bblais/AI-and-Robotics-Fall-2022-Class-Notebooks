#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def heuristic(state,player):
    # material advantage
    if player==1:
        other_player=2
    else:
        other_player=1
    
    
    # other_player=3-player  # this is terrible but works
    
    count=0
    for i in range(9):
        if state[i]==player:
            count+=1
    
    N_player=count
    
    
    count=0
    for i in range(9):
        if state[i]==other_player:
            count+=1
    
    N_other_player=count
    
    value = (N_player-N_other_player)/(N_player+N_other_player)
    

