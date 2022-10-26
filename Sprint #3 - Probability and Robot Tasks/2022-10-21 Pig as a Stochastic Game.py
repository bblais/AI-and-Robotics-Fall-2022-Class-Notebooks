#!/usr/bin/env python
# coding: utf-8

# ## Rules of Pig
# 
# 

# - moves:
#     - roll
#     - hold
# - goal to 100 points 
# - roll a die
#     - roll a 1 your turn is over, you get no points
#     - 2-6, add this number to your turn total      get another turn
# - hold:
#     - turn points get added to your total points, your turn is over

# In[1]:


from Game import *


# In[2]:


def initial_state():
    # player 1 score, player 2 score, turn score, last dice roll
    return [0,0,0,0]


# In[3]:


def valid_moves(state,player):
    return ["hold","roll"]


# In[4]:


def show_state(state):
    print("Player 1 score:",state[0])
    print("Player 2 score:",state[1])    
    print("Turn score:",state[2])    
    print("Last die:",state[3])    
    


# In[5]:


def win_status(state,player):
    goal=21
    
    player1_total,player2_total,turn_total,last_die=state
    
    if player==1:
        if player1_total + turn_total>=goal:
            return "win"
        
    elif player==2:
        if player2_total + turn_total>=goal:
            return "win"
    else:
        raise ValueError("You can't get there from here.")
        


# In[6]:


def update_state(state,player,move):
    new_state=state
    player1_total,player2_total,turn_total,last_die=state
    
    
    if move=="hold":
        if player==1:
            new_state[0]=player1_total+turn_total
        else:
            new_state[1]=player2_total+turn_total
        
        new_state[2]=0  # reset the turn total
        new_state[3]=0  # this resets the last die
        
    elif move=="roll":
        dice=random.randint(1,6)  # this generates a value from 1-6
        
        new_state[3]=dice
        if dice==1:
            new_state[2]=0  # reset the turn total
        else:
            new_state[2]=turn_total+dice  # update the turn total
        
    else:
        raise ValueError("You can't get there from here.")
        
    
    return new_state
    


# In[7]:


def repeat_move(state,player,move):
    player1_total,player2_total,turn_total,last_die=state

    # check for die roll of 1 or 0
    # check for turn total > 0
    
    if last_die==0 or last_die==1:
        return False
    else:
        return True
    


# In[8]:


def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)
 
random_agent=Agent(random_move)    


# In[9]:


def human_move(state,player):   
    
    move=input("Roll or Hold?").lower()
    
    if move[0]=='r':
        return "roll"
    else:
        return "hold"

human_agent=Agent(human_move)    


# In[10]:


g=Game()
g.run(human_agent,random_agent)


# In[ ]:




