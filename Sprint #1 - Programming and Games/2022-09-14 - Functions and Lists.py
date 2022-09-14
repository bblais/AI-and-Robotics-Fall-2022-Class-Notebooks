#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


def function_name(information_it_needs,more_information_it_needs):
    # code block doing all the stuff
    
    return results


# In[3]:


# function to calculate the length of the hypotenuse of a right triangle

You need the two sides:  $a$ and $b$.

do some math

$$
c=\sqrt{a^2+b^2}
$$
# You need the two sides:  $a$ and $b$.
# 
# do some math
# 
# $$
# c=\sqrt{a^2+b^2}
# $$

# In[6]:


def hypotenuse(a,b):
    from math import sqrt
    
    c=sqrt(a**2+b**2)
    
    return c


# In[7]:


hypotenuse(5,8)


# In[8]:


bob=hypotenuse(5,8)
sally=hypotenuse(3,4)
bob+sally


# # Data structure

# In[9]:


a=5
a


# In[10]:


type(a)


# In[11]:


b=5.5


# In[12]:


type(b)


# In[13]:


c='hello'


# In[15]:


type(c)


# In[16]:


c*5


# In[17]:


c="10"


# In[18]:


c*5


# In[20]:


d=[1,4,2,'bob','chickens',34.2]
d


# In[21]:


type(d)


# In[22]:


d[0]


# In[23]:


d[3]


# In[ ]:




