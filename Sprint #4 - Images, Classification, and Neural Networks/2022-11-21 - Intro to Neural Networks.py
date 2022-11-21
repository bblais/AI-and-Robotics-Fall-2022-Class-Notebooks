#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import *


# In[ ]:


from classy import *


# In[ ]:


data_train=double_moon_data(d=-2,N=1000)
data_test=double_moon_data(d=-2,N=200)


# In[ ]:


plot2D(data_train)


# ## no hidden layer, linear units = Perceptron

# In[ ]:


C=NumPyNetBackProp({
    'input':2,               # number of features
    'output':(2,'linear'),  # number of classes
    'cost':'mse',
})

# activation functions - linear, tanh (-1 to 1), logistic (0 to 1), relu (min 0, linear)


# In[ ]:


C.fit(data_train.vectors,data_train.targets,epochs=3000)


# In[ ]:


print((C.predict(data_test.vectors)))
print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[ ]:


plot2D(data_test,classifier=C)


# In[ ]:


data=load_excel('data/iris.xls')


# In[ ]:


subset=extract_features(data,[0,1])
plot2D(subset)


# In[ ]:


data_train,data_test=split(subset,test_size=0.2)


# In[ ]:


C=NumPyNetBackProp({
    'input':2,               # number of features
    'output':(3,'linear'),  # number of classes
    'cost':'mse',
})

# activation functions - linear, tanh (-1 to 1), logistic (0 to 1), relu (min 0, linear)


# In[ ]:


C.fit(data_train.vectors,data_train.targets,epochs=3000)


# In[ ]:


print((C.predict(data_test.vectors)))
print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[ ]:


plot2D(data_test,classifier=C)


# ## Backprop with hidden units

# In[ ]:


data_train=double_moon_data(d=-2,N=1000)
data_test=double_moon_data(d=-2,N=200)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


C=NumPyNetBackProp({
    'input':2,               # number of features
    'hidden':[(15,'logistic'),],
    'output':(2,'logistic'),  # number of classes
    'cost':'mse',
})


# In[ ]:


C.fit(data_train.vectors,data_train.targets,epochs=6000)


# In[ ]:


print((C.predict(data_test.vectors)))
print(("On Training Set:",C.percent_correct(data_train.vectors,data_train.targets)))
print(("On Test Set:",C.percent_correct(data_test.vectors,data_test.targets)))


# In[ ]:


plot2D(data_test,classifier=C)


# In[ ]:




