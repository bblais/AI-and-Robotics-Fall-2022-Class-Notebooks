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


# In[40]:


data_train,data_test=split(subset,test_size=0.2)


# In[41]:


C=NaiveBayes()


# In[42]:


C.fit(data_train.vectors,data_train.targets)


# In[43]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[44]:


C=kNearestNeighbor()
data_train,data_test=split(data,test_size=0.2)


# In[45]:


C.fit(data_train.vectors,data_train.targets)


# In[46]:


print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[ ]:





# ## Images
