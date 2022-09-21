#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


state=Board(3,3)


# In[3]:


state


# In[4]:


state[2]=3
state[1]=4


# In[5]:


state


# In[6]:


3 in state


# In[7]:


1 in state


# In[10]:


player=1
moves=[]

if player==1:
    for value in [1,3,5,7,9]:
        if not value in state:
            for location in range(9):
                if state[location]==0:
                    moves.append( [value,location])


# In[11]:


moves


# In[12]:


value=int(input("What value will you play?"))
location=int(input("What location to play?"))
move=[value,location]


# In[13]:


move


# In[15]:


state=Board(3,3)
for loc in [0,1,2]:
    state[loc]=1
for loc in [6,7,8]:
    state[loc]=2
    
state


# In[16]:


state.show_locations()


# In[23]:


def valid_moves(state,player):
    
    moves=[]
    if player==1:
        
        for start in [0,1,2,3,4,5]:
            if state[start]==1 and state[start+3]==0:
                moves.append( [start,start+3] )
            
#         if state[1]==1 and state[4]==0:
#             moves.append( [1,4] )       
            
#         if state[2]==1 and state[5]==0:
#             moves.append( [2,5] )       
            
            
    return moves


# In[22]:


valid_moves(state,1)


# In[ ]:




