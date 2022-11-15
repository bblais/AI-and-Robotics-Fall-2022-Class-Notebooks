#!/usr/bin/env python
# coding: utf-8

# In[13]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *
import os


# In[21]:


def get_subimage(im,r_value,c_value):
    
    # I assume you have this written and not return a random image
    return rand(200,300)


# In[15]:


ls images/*


# In[17]:


if not os.path.exists('squares'):
    os.mkdir('squares')


# In[18]:


filename='images/board images/test0.jpg'


# In[19]:


im=imread(filename)


# In[20]:


im.shape


# In[23]:


for r,c in [[0,2],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[2,4]]:
    print(r,c)
    subimage=get_subimage(im,r,c)
    imsave(f"squares/square {r} {c}.jpeg",subimage)


# In[24]:


from glob import glob


# In[25]:


board_filenames=glob('images/board images/*.jpg')


# In[28]:


for count,filename in enumerate(board_filenames):
    im=imread(filename)
    
    for r,c in [[0,2],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[2,4]]:
        subimage=get_subimage(im,r,c)
        subfilename=f"squares/square {count} {r} {c}.jpeg"
        print(r,c)
        print(subfilename)
        imsave(subfilename,subimage)    


# In[ ]:




