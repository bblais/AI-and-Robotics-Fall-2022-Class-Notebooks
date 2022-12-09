#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!pip install "git+https://github.com/bblais/Game" --upgrade
from Game import *


# In[3]:


def initial_state():
    state=Board(3,3,3)
    state[0]=1
    state[1]=1
    state[2]=2
    state[3]=2
    state[4]=2
    state[5]=1
    state[6]=1
    state[7]=2
    state[8]=1
    return state

#state[0]=1 in cases where we need to have starting pieces


# In[5]:


def valid_moves(state,player):
    
    moves=[]
    
    for location in range(27):
        if state[location]==0:
            moves.append(location)
            
    return moves


# In[7]:


def update_state(state,player,move):
    
    new_state = state
    
    new_state[move]=player
    
    return new_state


# In[8]:


def three_in_a_row(a,b,c,player):
    if a==player and b==player and c==player:
        return True
    else:
        return False
    
    
def win_status(state,player):
    
    if player==1:
        other_player=2
    else:
        other_player=1
    
    #Wins by rows (2D)
    if three_in_a_row(state[0],state[1],state[2],player):
        return 'win'
    if three_in_a_row(state[3],state[4],state[5],player):
        return 'win'
    if three_in_a_row(state[6],state[7],state[8],player):
        return 'win'
    
    if three_in_a_row(state[9],state[10],state[11],player):
        return 'win'
    if three_in_a_row(state[12],state[13],state[14],player):
        return 'win'
    if three_in_a_row(state[15],state[16],state[17],player):
        return 'win'
    
    if three_in_a_row(state[18],state[19],state[20],player):
        return 'win'
    if three_in_a_row(state[21],state[22],state[23],player):
        return 'win'
    if three_in_a_row(state[24],state[25],state[26],player):
        return 'win'
    
    #Wins by columns (2D)
    if three_in_a_row(state[0],state[3],state[6],player):
        return 'win'
    if three_in_a_row(state[1],state[4],state[7],player):
        return 'win'
    if three_in_a_row(state[2],state[5],state[8],player):
        return 'win'
    
    if three_in_a_row(state[9],state[12],state[15],player):
        return 'win'
    if three_in_a_row(state[10],state[13],state[16],player):
        return 'win'
    if three_in_a_row(state[11],state[14],state[17],player):
        return 'win'
    
    if three_in_a_row(state[18],state[21],state[24],player):
        return 'win'
    if three_in_a_row(state[19],state[22],state[25],player):
        return 'win'
    if three_in_a_row(state[20],state[23],state[26],player):
        return 'win'
    
    #Wins by diagonal (2D)
    if three_in_a_row(state[0],state[4],state[8],player):
        return 'win'
    if three_in_a_row(state[2],state[4],state[6],player):
        return 'win'
    
    if three_in_a_row(state[9],state[13],state[17],player):
        return 'win'
    if three_in_a_row(state[11],state[13],state[15],player):
        return 'win'
    
    if three_in_a_row(state[18],state[22],state[26],player):
        return 'win'
    if three_in_a_row(state[20],state[22],state[24],player):
        return 'win'
    
    #Wins by diagonal columns (3D)
    if three_in_a_row(state[0],state[12],state[24],player):
        return 'win'
    if three_in_a_row(state[6],state[12],state[18],player):
        return 'win'
    
    if three_in_a_row(state[1],state[13],state[25],player):
        return 'win'
    if three_in_a_row(state[7],state[13],state[19],player):
        return 'win'
    
    if three_in_a_row(state[2],state[14],state[26],player):
        return 'win'
    if three_in_a_row(state[8],state[14],state[20],player):
        return 'win'
    
    #Wins by diagonal rows (3D)
    if three_in_a_row(state[0],state[10],state[20],player):
        return 'win'
    if three_in_a_row(state[2],state[10],state[18],player):
        return 'win'
    
    if three_in_a_row(state[3],state[13],state[23],player):
        return 'win'
    if three_in_a_row(state[5],state[13],state[21],player):
        return 'win'
    
    if three_in_a_row(state[6],state[16],state[26],player):
        return 'win'
    if three_in_a_row(state[8],state[16],state[24],player):
        return 'win'
    
    #Wins by diagonal diagonals (3D)
    if three_in_a_row(state[0],state[13],state[26],player):
        return 'win'
    if three_in_a_row(state[2],state[13],state[24],player):
        return 'win'
    
    if three_in_a_row(state[6],state[13],state[20],player):
        return 'win'
    if three_in_a_row(state[8],state[13],state[18],player):
        return 'win'   
    
    if not valid_moves(state,other_player):
        return 'stalemate'
    
    #Wins if vertical
    if three_in_a_row(state[0],state[9],state[18],player):
        return 'win'
    if three_in_a_row(state[1],state[10],state[19],player):
        return 'win'
    if three_in_a_row(state[2],state[11],state[20],player):
        return 'win'
    if three_in_a_row(state[3],state[12],state[21],player):
        return 'win'
    if three_in_a_row(state[4],state[13],state[22],player):
        return 'win'
    if three_in_a_row(state[5],state[14],state[23],player):
        return 'win'
    if three_in_a_row(state[6],state[15],state[24],player):
        return 'win'
    if three_in_a_row(state[7],state[16],state[25],player):
        return 'win'
    if three_in_a_row(state[8],state[17],state[26],player):
        return 'win'
    
    
def show_state(state):
    print(state)
    


# In[9]:


def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)
 
random_agent=Agent(random_move)  


# In[10]:


from Game.minimax import *
def minimax_move(state,player):
    values,moves=minimax_values(state,player,display=True)
    return top_choice(moves,values)

minimax_agent=Agent(minimax_move)


# In[11]:


#Fix for Long Game

#Returns between -1 and 1 (not inclusive)
#Approximate value of a state
#+ = good
#- = bad


# In[12]:


#values,moves = minimax_values(1,1,display=True)
#values,moves


# In[13]:


def human_move(state,player):    
    print("""
    0  1  2 
    3  4  5
    6  7  8
    
       9   10  11
       12  13  14
       15  16  17
       
           18  19  20
           21  22  23
           24  25  26
    """)
    for i in range(5):
        move=int(input("What location do you want to move?"))
        if move in valid_moves(state,player):
            return move
        else:
            print("Illegal Move")
    return None
 
human_agent=Agent(human_move)  


# In[14]:


def skittles_move(state,player,info):
    T=info.T
    last_state=info.last_state
    last_action=info.last_action
    
    
    if state not in T:
        action=valid_moves(state,player)
        T[state]=Table()
        for action in action:
            T[state][action]=3  #number of skittles
    
    move=weighted_choice(T[state])
    
    if move is None:   # Can't win from this state
        if not last_state is None:
            T[last_state][last_action]-=1
            if T[last_state][last_action]<0:
                T[last_state][last_action]=0

        move=random_move(state,player)
    
    return move

def skittles_after(status,player,info):  # this is called after the game is over
    T=info.T
    last_state=info.last_state
    last_action=info.last_action
    
    if status == 'lose':
        T[last_state][last_action]-=1    # take away skittle
        if T[last_state][last_action]<0:
            T[last_state][last_action]=0
        


# In[ ]:





# In[15]:


#from TTT import *


# In[16]:


from Game.mcts import *
def mcts_move(state,player,info):
    T=info.T
    values,moves=mcts_values(state,player,T,info.seconds)
    return top_choice(moves,values)

mcts_agent=Agent(mcts_move)
mcts_agent.T=LoadTable(filename='mcts_data_3DTTT.json')
mcts_agent.seconds=1


# In[ ]:


def Q_move(state,player,info):
    Q=info.Q
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    
    α=info.α  # learning rate
    ϵ=info.ϵ  # how often to take a random move
    γ=info.γ  # memory constant -- how quickly does the table update back in time (earlier in the game)
    
    # \alpha <hit tab>    α
    # \epsilon <hit tab>  ϵ
    # \gamma <hit tab>    γ
    
    if state not in Q:
        actions=valid_moves(state,player)
        Q[state]=Table()
        for action in actions:
            Q[state][action]=0  # initial value of table
    
    if learning:
        if random.random()<ϵ:  # take a random move occasionally to explore the environment
            move=random_move(state,player)
        else:
            move=top_choice(Q[state])
    else:
        move=top_choice(Q[state])
    
    if not last_action is None:  # not the first move
        reward=0
        
        # learn
        if learning:
            Q[last_state][last_action]+=α*(reward +
                        γ*max([Q[state][a] for a in Q[state]]) - Q[last_state][last_action])
    
    return move


# In[ ]:


def Q_after(status,player,info):
    Q=info.Q
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    
    α=info.α  # learning rate
    ϵ=info.ϵ  # how often to take a random move
    γ=info.γ  # memory constant -- how quickly does the table update back in time (earlier in the game)
    
    # \alpha <hit tab>    α
    # \epsilon <hit tab>  ϵ
    # \gamma <hit tab>    γ

    if status=='lose':
        reward=-1
    elif status=='win':
        reward=1
    elif status=='stalemate':
        reward=.5 # value stalemate a little closer to a win
    else:
        reward=0
    
    
    if learning:
        Q[last_state][last_action]+=α*(reward - Q[last_state][last_action])
        


# In[ ]:


Q1_agent=Agent(Q_move)
Q1_agent.post=Q_after
Q1_agent.Q=Table()  # makes an empty table
Q1_agent.learning=True

Q1_agent.α=0.3  # learning rate
Q1_agent.ϵ=0.1  # how often to take a random move
Q1_agent.γ=0.9  # memory constant -- how quickly does the table update back in time (earlier in the game)


# In[ ]:


Q2_agent=Agent(Q_move)
Q2_agent.post=Q_after
Q2_agent.Q=Table()  # makes an empty table
Q2_agent.learning=True

Q2_agent.α=0.3  # learning rate
Q2_agent.ϵ=0.1  # how often to take a random move
Q2_agent.γ=0.9  # memory constant -- how quickly does the table update back in time (earlier in the game)


# In[ ]:





# In[ ]:





# In[ ]:




