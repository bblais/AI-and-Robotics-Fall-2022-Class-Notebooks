#!/usr/bin/env python
# coding: utf-8

# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[15]:


from classy import *


# In[16]:


images=image.load_images('images/board images/squares/')


# In[17]:


data=image.images_to_vectors(images,verbose=True)


# In[18]:


data.vectors


# In[19]:


from sklearn.cluster import KMeans


# In[27]:


kmeans = KMeans(n_clusters=3)
kmeans.fit(data.vectors)


# In[28]:


kmeans.labels_


# In[29]:


images.keys()


# In[30]:


count=1
figure(figsize=(20,20))
for im,label in zip(images.data,kmeans.labels_):
    subplot(5,5,count)
    imshow(im)
    count+=1
    axis('off')
    title(label)
    if count>25:
        break


# In[ ]:




