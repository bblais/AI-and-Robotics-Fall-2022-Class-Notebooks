#!/usr/bin/env python
# coding: utf-8

# In[8]:


from getpass import getpass
import xmlrpc.client
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
    arr_str=S.take_picture()
    arr=from_string(arr_str)
    return arr


# In[11]:


remote_host='dex.local'
remote_user='pi'
remote_password=getpass('Password:')


# In[12]:


from sshtunnel import SSHTunnelForwarder #Run pip install sshtunnel


# In[18]:


server=SSHTunnelForwarder(
    (remote_host, 22), #Remote server IP and SSH port
    ssh_username = remote_user,
    ssh_password = remote_password,
    remote_bind_address=(remote_host, 8002))  # <== needs to match the port on the robot


# In[19]:


server.start() #start ssh sever
print ('Server connected via SSH')


# In[20]:


local_port = str(server.local_bind_port)


# In[21]:


S=xmlrpc.client.ServerProxy('http://localhost:%s' % local_port)   


# In[9]:


arr=take_picture()
print(arr.shape)


# In[22]:


S.move_forward(10)


# In[23]:


server.is_active


# In[24]:


server.is_alive


# In[25]:


server.check_tunnels()


# In[26]:


server.restart()


# In[27]:


server.is_active


# In[28]:


server.check_tunnels()


# In[ ]:




