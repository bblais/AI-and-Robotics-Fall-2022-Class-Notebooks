#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[6]:


im=rand(288,352)


# In[7]:


imshow(im)


# In[12]:


def get_subimage(image,r,c):
    
    # r=0 50:120
    # r=1 130:190
    # r=2 200:260
    
    number_of_rows=70
    starting_row=50
    skip_rows=10
    
    r1=starting_row+(number_of_rows+skip_rows)*r
    r2=r1+number_of_rows
    
    
    # image[r1:r2,c1:c2]
    
    print(r1,r2)
    
    subimage=image[r1:r2,40:110]
    
    if r==0:
        if c==0:
            subimage=image[50:120,40:110]
        elif c==1:
            subimage=image[50:120,120:180]
            
    elif r==1:
        if c==0:
            subimage=image[130:190,40:110]
    
    
    return subimage


# In[18]:


subimage=get_subimage(im,2,1)


# In[9]:


imshow(subimage)


# In[ ]:




