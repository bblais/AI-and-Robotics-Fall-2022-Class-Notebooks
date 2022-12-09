#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Connect4 import *


# In[2]:


from Game.minimax import *
def minimax_move(state,player):
    values,moves=minimax_values(state,player,maxdepth=5,display=True)
    return top_choice(moves,values)
    
    
def heuristic(state,player):
    # count up the number of rows, columns, and diagonals 
    #where you occupy two spaces and the third space is empty. 
    #Then, subtract the number of rows, columns, and diagonals 
    #where your opponent occupies two spaces and the third space is empty. 
    #Finally, divide the result by the total number of rows, 
    # columns, and diagonals.    

    if player==1:
        other_player=2
    else:
        other_player=1
        
        
    total=0
    found=0
    
    for three in [state.diags(3),state.rows(3),state.cols(3)]:
        for d in three:
            if d.count(player)==2 and d.count(0)==1:
                found+=1
            if d.count(other_player)==2 and d.count(0)==1:
                found-=1
            total+=1

    return found/(total+1)
        

minimax_agent=Agent(minimax_move)


# In[3]:


g=Game(number_of_games=1)
g.display=False
results=g.run(minimax_agent,random_agent)
results


# In[ ]:




