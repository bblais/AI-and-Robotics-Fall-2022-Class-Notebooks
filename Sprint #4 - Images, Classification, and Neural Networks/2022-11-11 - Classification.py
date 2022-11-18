#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


from classy import *


# In[3]:


data=load_excel('data/iris.xls')


# In[4]:


plot2D(data)


# In[ ]:


subset=extract_features(data,[0,1])
plot2D(subset)


# In[8]:


data_train,data_test=split(data,test_size=0.2)


# In[9]:


C=NaiveBayes()


# In[10]:


C.fit(data_train.vectors,data_train.targets)


# In[11]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[12]:


C=kNearestNeighbor()


# In[13]:


C.fit(data_train.vectors,data_train.targets)


# In[14]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[ ]:





# ## Images

# In[59]:


images=image.load_images('images/all_pieces/')


# In[60]:


data=image.images_to_vectors(images)


# In[61]:


data_train,data_test=split(data,test_size=0.2)


# In[62]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[63]:


C=kNearestNeighbor()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# ## Predict

# In[64]:


test_square=image.load_images('images/square example.png')


# In[65]:


test_data=image.images_to_vectors(test_square)


# In[66]:


predictions=C.predict(test_data.vectors)
category=images.target_names[predictions[0]]
print(category)


# In[69]:


imshow(test_square.data[0])


# ## visualize

# In[20]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)


# In[21]:


C.means


# In[22]:


C.means.shape


# In[23]:


mean0=C.means[0,:]


# In[24]:


mean0.shape


# In[25]:


im0=mean0.reshape((57,66,4))


# In[26]:


im0.shape


# In[27]:


imshow(im0/im0.max())


# In[28]:


mean1=C.means[1,:]
im1=mean1.reshape((57,66,4))
im1=im1/im1.max()
imshow(im1)


# In[29]:


mean1=C.means[2,:]
im1=mean1.reshape((57,66,4))
im1=im1/im1.max()
imshow(im1)


# In[ ]:





# In[ ]:




