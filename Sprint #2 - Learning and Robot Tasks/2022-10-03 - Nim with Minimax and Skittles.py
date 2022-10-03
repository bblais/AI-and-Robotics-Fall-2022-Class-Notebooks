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


# In[42]:


def skittles_move(state,player,info):
    T=info.T
    last_state=info.last_state
    last_action=info.last_action
    
    
    if state not in T:
        actions=valid_moves(state,player)
        T[state]=Table()
        for action in actions:
            T[state][action]=3  # number of skittles
        
    
    move=weighted_choice(T[state])
    
    if move is None:  # can't win from this state
        if not last_state is None:
            T[last_state][last_action]-=1   # take away a skittle
            if T[last_state][last_action]<0:
                T[last_state][last_action]=0
    
        move=random_move(state,player)
    
    return move

def skittles_after(status,player,info):  # this is called after the game is over
    T=info.T
    last_state=info.last_state
    last_action=info.last_action

    if status=='lose':
        T[last_state][last_action]-=1   # take away a skittle
        if T[last_state][last_action]<0:
            T[last_state][last_action]=0
    
    


# In[20]:


skittles_agent=Agent(skittles_move)
skittles_agent.T=Table()
skittles_agent.post=skittles_after


# In[ ]:





# In[ ]:





# ### some debugging

# In[14]:


T=Table()
T


# In[15]:


state=6
T[state]=Table()

action=3
T[state][action]=3  # number of skittles
action=2
T[state][action]=3  # number of skittles
action=1
T[state][action]=3  # number of skittles

state=5
T[state]=Table()

action=3
T[state][action]=3  # number of skittles
action=2
T[state][action]=3  # number of skittles
action=1
T[state][action]=3  # number of skittles

T


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## Running the Game

# In[27]:


g=Game()
g.run(skittles_agent,random_agent)


# In[28]:


skittles_agent.T


# In[37]:


g=Game(number_of_games=100)
g.display=False
result=g.run(skittles_agent,random_agent)


# In[38]:


result.count(1),result.count(2)


# In[39]:


skittles_agent.T


# In[40]:


g=Game(number_of_games=100)
g.display=False
result=g.run(random_agent,skittles_agent)
result.count(1),result.count(2)


# In[43]:


skittles_agent=Agent(skittles_move)
skittles_agent.T=Table()
skittles_agent.post=skittles_after

g=Game(number_of_games=10000)
g.display=False
result=g.run(skittles_agent,skittles_agent)
result.count(1),result.count(2)


# In[44]:


skittles_agent.T


# In[ ]:




