#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# # Breakthrough

# In[40]:


def initial_state():
    N=8
    state=Board(N,N)
    
    for i in range(N):
        state[i]=2
    for i in range(N**2-N,N**2):
        state[i]=1
    return state


# In[41]:


state=initial_state()
state


# In[42]:


state.show_locations()


# In[43]:


state.shape


# In[44]:


N=8
list(range(N**2-1,N**2-N-1,-1))


# In[45]:


list(range(N**2-N,N**2))


# In[49]:


def valid_moves(state,player):
    N=state.shape[0]
    
    if player==1:
        other_player=2
    else:
        other_player=1
    
    # types of moves for breakthrough
    moves=[]
    
    if player==1:
        
        # north move
        for start in range(N,N**2):
            end=start-N
            
            if state[end]==0 and state[start]==player:
                moves.append([start,end])
              
        # north east move            
        for start in range(N,N**2):
            end=start-N+1  # start - (N-1)
                
            
            if (start+1) % 8 == 0:
                continue
                
            if state[end]==other_player and state[start]==player:
                moves.append([start,end])

                
        # north west move            
        for start in range(N,N**2):
            end=start-N-1  
                

            if start % 8 == 0:
                continue
                
            if state[end]==other_player and state[start]==player:
                moves.append([start,end])
                
                
    else:
        
        for start in range(N**2-N):
            end=start+N
            
            if state[end]==0 and state[start]==player:
                moves.append([start,end])
      
    
    
    
    return moves


# In[47]:


valid_moves(initial_state(),1)


# In[48]:


valid_moves(initial_state(),2)


# In[ ]:





# In[52]:


state.moves(1,"n","ne","nw")


# ## Connect Four

# In[53]:


def initial_state():
    M,N=6,7
    state=Board(M,N)
    
    return state


# In[56]:


state=initial_state()
state


# In[57]:


state.show_locations()


# In[62]:


def valid_moves(state,player):
    M,N=state.shape
    moves=[]
    for i in range(N):
        if state[0,i]==0:
            moves.append(i)
    
    return moves


# In[63]:


valid_moves(state,1)


# In[ ]:


def index_from_rc(r,c,M,N):
    index=r*N+c
    
    return index
    


# In[65]:


# another way to think of it -- the locations where it is filled up to
def valid_moves(state,player):
    M,N=6,7
    #M,N=state.shape
    moves=[]
    for c in range(N):
        for r in range(M-1,-1,-1):
            index=index_from_rc(r,c,M,N)
            if state[index]==0:
                moves.append(index)
                break
    
    return moves


# In[70]:


s1=[1,2,3]
s2=[1,0,3]


# In[73]:


s=[state[0],state[1],state[2]]
if sum(s)==15 and prod(s)>0:
    pass


# In[ ]:





# In[72]:


sum(s1),prod(s1)


# In[66]:


valid_moves(initial_state(),1)


# In[67]:


state=initial_state()
for i in [35,28,38,39]:
    state[i]=1
    
state


# In[68]:


state.show_locations()


# In[69]:


valid_moves(state,1)


# In[ ]:




