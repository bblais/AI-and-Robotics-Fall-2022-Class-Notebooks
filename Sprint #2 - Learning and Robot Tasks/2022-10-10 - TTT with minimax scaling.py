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


# In[4]:


def update_state(state,player,move):
    
    new_state=state
    
    new_state[move]=player
    
    return new_state


# In[5]:


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


# In[6]:


def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)
 
random_agent=Agent(random_move)    


# In[7]:


def human_move(state,player):    
    print("""
    0 1 2
    3 4 5
    6 7 8
    """)
    move=int(input("What location do you want to move?"))
    return move
 
human_agent=Agent(human_move)    


# In[8]:


from Game.minimax import *
def minimax_move(state,player):
    values,moves=minimax_values(state,player,maxdepth=20,display=True,cache=False)
    return top_choice(moves,values)
    
def heuristic(state,player):
    # returns between -1 and 1 (not inclusive)
    # approximate value of a state
    # positive = good for the player
    # negative = bad for player
    
    return 0

# material advantage
def heuristic(state,player):
    # returns between -1 and 1 (not inclusive)
    # approximate value of a state
    # positive = good for the player
    # negative = bad for player
    
    # count up my pieces, count up their pieces
    N_player=count_pieces(state,player)
    N_other=count_pieces(state,other_player)
    
    return (N_player-N_other)/(N_player+N_other)
    
    
    
    return 0




minimax_agent=Agent(minimax_move)


# In[9]:


g=Game()
g.run(minimax_agent,random_agent)


# The first time it sees the initial state it takes 0.7 seconds to solve.  the second time it sees it,

# In[10]:


g=Game()
g.run(minimax_agent,random_agent)


# it only takes 0.00055 seconds.  that's because of caching.  to really test minimax speed, we need to turn caching off in the minimax move (first introduced in version 0.2.37).  You need to restart the kernel and replace the minimax move with this version:

# In[9]:


def minimax_move(state,player):
    values,moves=minimax_values(state,player,maxdepth=20,display=True,cache=False)
    return top_choice(moves,values)


# In[11]:


g=Game()
g.run(minimax_agent,random_agent)


# In[12]:


g=Game()
g.run(minimax_agent,random_agent)


# a bit more direct to test, make the state mid-game.  for TTT the depth is 6 and the breadth is around 9 to start, and gets smaller.  Seems like it takes 2 seconds for the first move.  let's test this by making an initial state.

# In[14]:


state=initial_state()
print(state)
player=1
values=minimax_values(state,player,display=True,cache=False)


# 2nd move takes how long?  (depth of 8, breadth starts at 8)

# In[17]:


state=initial_state()
state[0]=1
print(state)
player=2
values=minimax_values(state,player,display=True,cache=False)


# 3rd move how long?

# In[16]:


state=initial_state()
state[0]=1
state[2]=2
print(state)
player=1
values=minimax_values(state,player,display=True,cache=False)


# and on....

# In[22]:


player=1
other_player=2
state=initial_state()
for i in range(9):
    print(state)
    values=minimax_values(state,player,display=True,cache=False)
    state[i]=player
    player,other_player=other_player,player
    


# In[26]:


x=range(9)
y=[2.07,0.2913,0.1487,0.04204893112182617,0.008081197738647461,
  0.0018281936645507812,0.0003509521484375,0.00021195411682128906,7.605e-05]


# In[27]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[28]:


plot(x,y,'-o')


# In[30]:


semilogy(x,y,'-o')


# linear on a log plot is exponential!

# In[ ]:




