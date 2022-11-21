#!/usr/bin/env python
# coding: utf-8

# In[24]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[25]:


from classy import *


# In[26]:


data_train=double_moon_data(d=-2,N=1000)
data_test=double_moon_data(d=-2,N=200)


# In[27]:


plot2D(data_train)


# ## no hidden layer, linear units = Perceptron

# In[28]:


C=NumPyNetBackProp({
    'input':2,               # number of features
    'output':(2,'linear'),  # number of classes
    'cost':'mse',
})

# activation functions - linear, tanh (-1 to 1), logistic (0 to 1), relu (min 0, linear)


# In[29]:


C.fit(data_train.vectors,data_train.targets,epochs=3000)


# In[30]:


print((C.predict(data_test.vectors)))
print(("On Train`ing Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[31]:


C.weights


# In[ ]:





# In[ ]:





# In[9]:


plot2D(data_test,classifier=C)


# In[32]:


data=load_excel('data/iris.xls')


# In[33]:


subset=extract_features(data,[0,1])
plot2D(subset)


# In[34]:


data_train,data_test=split(subset,test_size=0.2)


# In[35]:


C=NumPyNetBackProp({
    'input':2,               # number of features
    'output':(3,'linear'),  # number of classes
    'cost':'mse',
})

# activation functions - linear, tanh (-1 to 1), logistic (0 to 1), relu (min 0, linear)


# In[36]:


C.fit(data_train.vectors,data_train.targets,epochs=3000)


# In[37]:


print((C.predict(data_test.vectors)))
print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[38]:


C.weights


# In[ ]:





# In[17]:


plot2D(data_test,classifier=C)


# ## Backprop with hidden units

# In[18]:


data_train=double_moon_data(d=-2,N=1000)
data_test=double_moon_data(d=-2,N=200)


# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:


C=NumPyNetBackProp({
    'input':2,               # number of features
    'hidden':[(15,'logistic'),],
    'output':(2,'logistic'),  # number of classes
    'cost':'mse',
})


# In[20]:


C.fit(data_train.vectors,data_train.targets,epochs=6000)


# In[21]:


print((C.predict(data_test.vectors)))
print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[22]:


plot2D(data_test,classifier=C)


# In[23]:


C.weights


# In[ ]:




