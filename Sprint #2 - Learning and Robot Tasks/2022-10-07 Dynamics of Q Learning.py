#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
from Game import Storage


# In[2]:


reward=1
α=0.1

# \alpha  then hit TAB then you get α


S=Storage()

Q=0
S+=Q,
for i in range(100):
    Q+=α*(reward-Q)
    S+=Q,

    
Q=S.arrays()


# In[3]:


plot(Q)


# In[4]:


reward=1
α=0.1

S=Storage()

Q1=Q2=Q3=0
S+=Q1,Q2,Q3
for i in range(50):
    Q1+=α*(reward-Q1)
    Q2+=.2*(reward-Q2)
    Q3+=.3*(reward-Q3)
    S+=Q1,Q2,Q3

    
Q1,Q2,Q3=S.arrays()
plot(Q1)
plot(Q2)
plot(Q3)


# In[5]:


reward=-1
α=0.1

S=Storage()

Q1=Q2=Q3=0
S+=Q1,Q2,Q3
for i in range(50):
    Q1+=α*(reward-Q1)
    Q2+=.2*(reward-Q2)
    Q3+=.3*(reward-Q3)
    S+=Q1,Q2,Q3

    
Q1,Q2,Q3=S.arrays()
plot(Q1)
plot(Q2)
plot(Q3)


# In[6]:


α=0.1

S=Storage()

Q1=Q2=Q3=0
S+=Q1,Q2,Q3
for i in range(50):
    
    if rand()<0.2:
        reward=-1
    else:
        reward=+1
    
    
    
    Q1+=α*(reward-Q1)
    Q2+=.2*(reward-Q2)
    Q3+=.3*(reward-Q3)
    S+=Q1,Q2,Q3

    
Q1,Q2,Q3=S.arrays()
plot(Q1)
plot(Q2)
plot(Q3)


# In[7]:


α=0.1

S=Storage()

Q1=0
S+=Q1,
for i in range(5000):
    
    if rand()<0.2:
        reward=-1
    else:
        reward=+1
    
    
    
    Q1+=α*(reward-Q1)
    S+=Q1,

    
Q1=S.arrays()
plot(Q1)

plot([0,len(Q1)],[mean(Q1),mean(Q1)])


# In[8]:


α=0.01

S=Storage()

Q1=0
S+=Q1,
for i in range(5000):
    
    if rand()<0.2:
        reward=-1
    else:
        reward=+1
    
    
    
    Q1+=α*(reward-Q1)
    S+=Q1,

    
Q1=S.arrays()
plot(Q1)

plot([0,len(Q1)],[mean(Q1),mean(Q1)])


# In[15]:


.2*-1+.8*1


# In[ ]:




