#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xmlrpc.client
import ssl

from time import sleep

def to_string(arr):
    import json
    s=json.dumps(arr.tolist())
    return s

def from_string(s):
    import json
    from numpy import array
    arr=array(json.loads(s))
    return arr


def take_picture():
    s=server.take_picture()
    arr=from_string(s)
    return arr
    

server=xmlrpc.client.ServerProxy('http://localhost:4001')    

arr=take_picture()
print(arr.shape)


# In[ ]:




