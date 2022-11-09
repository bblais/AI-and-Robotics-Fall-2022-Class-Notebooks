#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


from pylab import *  # super lazy


# https://www.theverge.com/2021/4/12/22379880/artificial-intelligence-cat-photos-gan
# 
# https://thiscatdoesnotexist.com/
# 
# 
# A cool seminar on colormaps:  https://youtu.be/xAoljeRJ3lU

# In[12]:


im=imread('images/cats.jpg')


# In[13]:


imshow(im)


# In[14]:


im


# In[15]:


im.shape


# In[16]:


im[1,2,0]


# In[17]:


im[1:11,2,0]


# In[19]:


im[1:11,2:18,0]


# In[21]:


subimage=im[1:11,2:18,:]


# In[22]:


imshow(subimage)


# In[23]:


imshow(im)


# In[24]:


subimage=im[0:400,1100:1500, :  ]
imshow(subimage)


# In[26]:


subimage=im[0:400,1100:1500, 0  ]
imshow(subimage)
colorbar()


# In[27]:


subimage=im[0:400,1100:1500, 1  ]
imshow(subimage)
colorbar()


# In[28]:


subimage=im[0:400,1100:1500, 2  ]
imshow(subimage)
colorbar()


# In[29]:


im2=imread('images/bird.png')


# In[30]:


imshow(im2)


# In[31]:


im2.shape


# In[33]:


subimage2=im2[:,:, 0  ]
imshow(subimage2)
colorbar()


# In[35]:


subimage2=im2[:,:, 3  ]
imshow(subimage2)
colorbar()


# In[ ]:




