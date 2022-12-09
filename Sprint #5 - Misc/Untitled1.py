#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xmlrpc.client


# In[6]:


server=xmlrpc.client.ServerProxy('http://192.168.2.3:8080')


# In[7]:


server.your_method_name()


# In[ ]:




