#!/usr/bin/env python
# coding: utf-8

# In[3]:


def factorial(N):
    
    value=N*factorial(N-1)
    
    return value


# Recursive definition of factorial
# $$
# N! = N \cdot (N-1)!
# $$
# 
# $$
# 0! = 1
# $$
# 
# Need a stop condition or you get an infinite loop.

# In[4]:


factorial(5)


# In[7]:


def factorial_fixed(N):
    
    if N==0:
        value=1
    else:
        value=N*factorial_fixed(N-1)
        
    return value


# In[8]:


factorial_fixed(5)


# In[ ]:




