#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# ## Game functions

# In[2]:


def initial_state():
    return 21


# In[3]:


def valid_moves(state,player):
    if state==1:
        return [1]
    elif state==2:
        return [1,2]
    else:
        return [1,2,3]
    


# In[4]:


def update_state(state,player,move):
    
    new_state=state-move
    
    return new_state


# In[5]:


def show_state(state):
    number_of_sticks=state
    print("The number of sticks is ",number_of_sticks)


# In[6]:


def win_status(state,player):

    # the state here is the state after the player made the move
    
    # returns  - 'win'  if the state is a winning state for the player, 
    #            'lose' if the state is a losing state for the player,
    #            'stalemate' for a stalemate
    #            None otherwise    
    
    
    if state==1:
        return "win"
    
    if state==0:
        return "lose"
    
    


# ## Agents

# In[7]:


def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)
 
random_agent=Agent(random_move)    


# In[8]:


def human_move(state,player):    
    move=int(input("How many sticks to take?"))
    return move
 
human_agent=Agent(human_move)    


# In[9]:


from Game.minimax import *
def minimax_move(state,player):
    values,moves=minimax_values(state,player,display=True)
    return top_choice(moves,values)
    
    
    
minimax_agent=Agent(minimax_move)


# Fix for long games

# In[12]:


from Game.minimax import *
def minimax_move(state,player):
    values,moves=minimax_values(state,player,maxdepth=5,display=True)
    return top_choice(moves,values)
    
def heuristic(state,player):
    # returns between -1 and 1 (not inclusive)
    # approximate value of a state
    # positive = good for the player
    # negative = bad for player
    
    if state%2==0:   # even state
        return 0.3
    else:  # odd state
        return -0.3
    
minimax_agent=Agent(minimax_move)


# ### Long Game

# In[16]:


values,moves=minimax_values(200,1,display=True)
values,moves


# In[15]:


values,moves=minimax_values(100000,1,maxdepth=5,display=True)  # need a heuristic function to deal with recursion
values,moves


# ## Running the Game

# In[18]:


g=Game()
g.run(human_agent,minimax_agent)


# In[ ]:




