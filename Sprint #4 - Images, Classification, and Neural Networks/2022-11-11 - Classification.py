#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


from classy import *


# In[11]:


data=load_excel('data/iris.xls')


# In[12]:


plot2D(data)


# In[15]:


subset=extract_features(data,[0,1])
plot2D(subset)


# In[56]:


data_train,data_test=split(data,test_size=0.2)


# In[57]:


C=NaiveBayes()


# In[58]:


C.fit(data_train.vectors,data_train.targets)


# In[59]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[60]:


C=kNearestNeighbor()


# In[61]:


C.fit(data_train.vectors,data_train.targets)


# In[62]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[ ]:





# ## Images

# In[64]:


images=image.load_images('images/all_pieces/')


# In[66]:


data=image.images_to_vectors(images)


# In[67]:


data_train,data_test=split(data,test_size=0.2)


# In[70]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[71]:


C=kNearestNeighbor()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# ## visualize

# In[72]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)


# In[73]:


C.means


# In[74]:


C.means.shape


# In[75]:


mean0=C.means[0,:]


# In[76]:


mean0.shape


# In[77]:


im0=mean0.reshape((57,66,4))


# In[78]:


im0.shape


# In[81]:


imshow(im0/im0.max())


# In[82]:


mean1=C.means[1,:]
im1=mean1.reshape((57,66,4))
im1=im1/im1.max()
imshow(im1)


# In[83]:


mean1=C.means[2,:]
im1=mean1.reshape((57,66,4))
im1=im1/im1.max()
imshow(im1)


# In[ ]:




