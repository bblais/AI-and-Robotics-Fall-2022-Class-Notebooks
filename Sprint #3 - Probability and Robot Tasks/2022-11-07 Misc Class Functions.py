#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def state_to_observation(state,player):
    deck,hand1,hand2=state
    
    if player==1:
        observation=hand1,hand2[1:]  
        
    else:
        observation=hand2,hand1[1:]
        
    
    return observation


# In[ ]:


def show_state(observation):
    
    myhand,other_hand=observation
    
    print("My hand:",myhand)
    print("Other hand:",other_hand)    


# In[1]:


def initial_state():
    # player 1 score, player 2 score, turn score, last dice roll1 last dice roll 2
    return [0,0,0,0,0]

def valid_moves(state,player):
    if state[3]==state[4]:  # last two rolls the same
        return ["roll"]
    else:
        return ["hold","roll"]


# In[4]:


state=["rock","paper","scissors","rock"]


# In[5]:


player1_move=state[-2]
player2_move=state[-1]


# In[6]:


player1_move


# In[7]:


player2_move


# In[ ]:


if player==1:
    return None


# In[ ]:


if player1_move=="scissors" and player2_move=="rock":
    #  all wins/losses are phrased in terms of player 2
    return "win"
elif .....

