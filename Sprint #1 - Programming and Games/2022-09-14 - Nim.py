#!/usr/bin/env python
# coding: utf-8
These functions need to be named exactly this:

initial_state - 
    takes in - Nothing
    returns  - The initial state of the game
    
win_status - 
    takes in - the state and the player
    returns  - 'win'  if the state is a winning state for the player, 
               'lose' if the state is a losing state for the player,
               'stalemate' for a stalemate
               None otherwise
               
valid_moves
    takes in - the state and the player
    returns  - a list of the valid moves for the state and player
    
    
update_state - 
    takes in - the state, the player, and the move
    returns  - the new state after the move for the player

show_state - 
    takes in - the state
    returns nothing, but prints out the current state (i.e. draws the board)


This function is optional:

repeat_move - 
    takes in - the state, the player, and the move
    returns  - True, if the current player gets another move right 
               after this one.  returns False otherwise.

This function can be named something else:

my_agent_move - 
    takes in - the state and the player (optionally the agent info)
    returns - a valid move
   
Example agent:

def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)
    
    
random_agent=Agent(random_move)

Usage - 

my_agent=Agent(my_agent_move)
    
g=Game(number_of_games=1000)
g.run(my_agent,random_agent)
g.report()  # writes out percentage of wins, etc...


# In[1]:


from Game import *


# In[2]:


def initial_state():
    return 21


# In[6]:


def valid_moves(state,player):
    if state==1:
        return [1]
    elif state==2:
        return [1,2]
    else:
        return [1,2,3]
    


# In[7]:


valid_moves(21,1)


# In[8]:


valid_moves(2,1)


# In[9]:


def update_state(state,player,move):
    
    new_state=state-move
    
    
    return new_state


# In[10]:


update_state(13,1,2)


# In[11]:


update_state(13,1,20)


# In[ ]:




