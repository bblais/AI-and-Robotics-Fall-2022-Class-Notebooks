#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


def initial_state():
    state=Board(3,3)
    
    # state[0]=1 in cases where we need to have starting pieces
    return state


# In[3]:


def valid_moves(state,player):
    
    # nope -- return [0,1,2,3,4,5,6,7,8]
    
    EMPTY=0
    X=1
    O=2
    
    moves=[]
    
    if state[0]==0:
        moves.append(0)
    if state[1]==0:
        moves.append(1)        
    if state[2]==0:
        moves.append(2)
        
    #....
    
    moves=[]
    for location in range(9):
        if state[location]==EMPTY:
            moves.append(location)
    
    
    return moves


# In[5]:


def update_state(state,player,move):
    
    new_state=state
    
    new_state[move]=player
    
    return new_state


# In[6]:


def three_in_a_row(a,b,c,player):
    
    if a==player and b==player and c==player:
        return True
    else:
        return False
    
    
    
def win_status(state,player):
    
    # 0 1 2
    # 3 4 5
    # 6 7 8
    
    if player==1:
        other_player=2
    else:
        other_player=1
    
    if three_in_a_row(state[0],state[1],state[2],player):
        return 'win'
    if three_in_a_row(state[3],state[4],state[5],player):
        return 'win'
    if three_in_a_row(state[6],state[7],state[8],player):
        return 'win'
    if three_in_a_row(state[0],state[3],state[6],player):
        return 'win'
    if three_in_a_row(state[1],state[4],state[7],player):
        return 'win'
    if three_in_a_row(state[2],state[5],state[8],player):
        return 'win'
    if three_in_a_row(state[0],state[4],state[8],player):
        return 'win'
    if three_in_a_row(state[2],state[4],state[6],player):
        return 'win'
    
    if not valid_moves(state,other_player):
        return 'stalemate'
    
    
def show_state(state):
    print(state)
    
    
    
def show_state(state):
    
    for i in range(9):
        if state[i]==1:
            print(" X ",end="")
        elif state[i]==2: 
            print(" O ",end="")
        else:
            print(" . ",end="")
            
        if i==2 or i==5:
            print()


# In[10]:


def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)
 
random_agent=Agent(random_move)    


# In[11]:


def human_move(state,player):    
    print("""
    0 1 2
    3 4 5
    6 7 8
    """)
    move=int(input("What location do you want to move?"))
    return move
 
human_agent=Agent(human_move)    


# In[12]:


from Game.minimax import *
def minimax_move(state,player):
    values,moves=minimax_values(state,player,maxdepth=20,display=True)
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


# In[14]:


g=Game()
g.run(minimax_agent,random_agent)


# In[16]:


state=initial_state()
state[0]=1
state[1]=2
values,moves=minimax_values(state,1,display=True)
values,moves


# In[ ]:




