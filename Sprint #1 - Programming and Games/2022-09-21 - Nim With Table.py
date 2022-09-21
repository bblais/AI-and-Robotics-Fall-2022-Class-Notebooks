#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


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
    
    


# In[30]:


def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)
 
random_agent=Agent(random_move)    


# In[31]:


def human_move(state,player):
    
    for i range(5):
        move=int(input("How many sticks to take?"))

        if move in valid_moves(state,player):
            return move
        else:
            print("Illegal move.")

    return None
        
human_agent=Agent(human_move)    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


def make_nim_table():
    T=Table()

    state=3
    T[state]=Table()
    
    
    return T


# In[ ]:


def table_move(state,player):
    T=make_nim_table()
    move=top_choice(T[state])
    return move

table_agent=Agent(table_move)


# In[ ]:





# In[32]:


g=Game()
g.run(human_agent,random_agent)


# In[ ]:




