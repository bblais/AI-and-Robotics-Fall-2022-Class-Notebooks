#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[2]:


from classy import *


# In[3]:


images=image.load_images('images/all_pieces/')


# In[4]:


data=image.images_to_vectors(images)


# In[5]:


data_train,data_test=split(data,test_size=0.2)


# ## Naive Bayes

# In[6]:


C=NaiveBayes()
C.fit(data_train.vectors,data_train.targets)
print("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets))
print("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets))


# In[7]:


C.means


# In[8]:


C.means.shape


# In[9]:


mean0=C.means[0,:]


# In[10]:


mean0.shape


# In[11]:


im0=mean0.reshape((57,66,4))


# In[12]:


imshow(im0/im0.max())


# ## Perceptron

# In[13]:


data_train.vectors.shape


# In[14]:


number_of_features=data_train.vectors.shape[1]
number_of_categories=3  # the types of pieces


# In[15]:


C=NumPyNetBackProp({
    'input':number_of_features,               # number of features
    'output':(number_of_categories,'linear'),  # number of classes
    'cost':'mse',
})


# In[16]:


C.fit(data_train.vectors,data_train.targets,epochs=500)   # you'll want to increase epochs here


# In[17]:


print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[18]:


len(C.weights)


# In[ ]:


C.weights[0]  # first layer


# In[19]:


W=C.weights[0]
W.shape


# In[20]:


vec=W[:,0]
vec=(vec-W.min())/(W.max()-W.min())  # rescale to 0-1
im=vec.reshape((57,66,4))
imshow(im)


# for non-linear perceptron, change the output function, like

# In[ ]:


C=NumPyNetBackProp({
    'input':number_of_features,               # number of features
    'output':(number_of_categories,'logistic'),  # number of classes
    'cost':'mse',
})


# for non-linear backprop, you add layers, like

# In[ ]:


C=NumPyNetBackProp({
    'input':number_of_features,               # number of features
    'hidden':[(15,'logistic'),],   # this size is "arbitrary"
    'output':(number_of_categories,'logistic'),  # number of classes
    'cost':'mse',
})

