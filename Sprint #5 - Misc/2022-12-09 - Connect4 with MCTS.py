#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Connect4 import *


# In[2]:


from Game.mcts import *
def mcts_move(state,player,info):
    T=info.T
    values,moves=mcts_values(state,player,T,info.seconds)
    return top_choice(moves,values)

mcts_agent=Agent(mcts_move)
mcts_agent.T=LoadTable(filename='mcts_data_TTT.json')
mcts_agent.seconds=1


# In[3]:


g=Game()
g.display=True
wins=g.run(mcts_agent,random_agent)
g.report()

SaveTable(mcts_agent.T,filename='mcts_data_TTT.json')


# In[21]:


def get_move(state,player):
    from copy import deepcopy
    
    if player==1:
        other_player=2
    else:
        other_player=1
    
    # check for easy win, which should get rewarded later
    winning_move=easy_win(state,player)
    if not winning_move is None:
        move=winning_move
        return move
    else:
        # for TTT and connect4 the moves are symmetrical between the players
        # so you can look to block easy wins for the other player
        # this wont work for any other game.
        blocking_move=easy_win(state,other_player)
        if not blocking_move is None:
            move=blocking_move
            return move
    
    
    T=LoadTable("mcts_data_TTT.json")
    moves=valid_moves(state,player)
    available_states=[update_state(deepcopy(state),player,move)
                                    for move in moves] 
    
    for S in available_states:
        if (S,player) not in T:
            T[(S,player)]={'wins':0,'plays':1}

    values=[float(T[(S,player)]['wins'])/T[(S,player)]['plays'] for S in available_states]
    values,moves=mysort(values,moves,reverse=True)
    
    return top_choice(moves,values)


# In[22]:


get_move(initial_state(),1)


# In[11]:


initial_state().shape


# In[12]:


state=initial_state()


# In[23]:


state.board=[
    0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,
    1,0,0,0,0,0,0,
    1,0,2,2,0,0,0,
    2,0,1,1,2,1,0,
    1,2,2,2,1,2,1,
]


# In[24]:


state


# In[25]:


easy_win(state,2)


# In[26]:


get_move(state,1)


# In[ ]:




