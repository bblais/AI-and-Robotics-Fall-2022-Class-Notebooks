#!/usr/bin/env python
# coding: utf-8

# In[1]:


from getpass import getpass
import paramiko


# In[4]:


ssh_host='localhost'
ssh_user='bblais'
ssh_password=getpass('Password:')


# In[5]:


ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect(hostname=ssh_host, username=ssh_user, password=ssh_password)


# In[6]:


remote_host='localhost'
remote_port=4001


# In[10]:


transport = ssh.get_transport()
dest_addr = (remote_host, remote_port)
local_unique_port = 8002 # any unused local port
local_host = 'localhost'
local_addr = (local_host, local_unique_port)


# In[15]:


transport.request_port_forward("localhost", 8080, "http://localhost/", 8000)
transport.request_dynamic_port_forward("localhost", 0)


# In[16]:


get_ipython().run_line_magic('pinfo', 'transport.request_port_forward')


# In[11]:


channel = transport.open_channel("direct-tcpip", dest_addr, local_addr)


# In[13]:


dest_addr


# In[14]:


local_addr


# In[ ]:





# In[ ]:





# In[6]:


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
    s=server.take_picture()
    arr=from_string(s)
    return arr


# In[4]:


remote_host='localhost'
remote_user='bblais'
remote_password=getpass('Password:')


# In[9]:


from sshtunnel import SSHTunnelForwarder #Run pip install sshtunnel


# In[10]:


with SSHTunnelForwarder(
    (remote_host, 22), #Remote server IP and SSH port
    ssh_username = remote_user,
    ssh_password = remote_password,
    remote_bind_address=(remote_host, 4001)) as server: #PostgreSQL server IP and sever port on remote machine
        
    server.start() #start ssh sever
    print ('Server connected via SSH')
    
    #connect to PostgreSQL
    local_port = str(server.local_bind_port)
    
    server=xmlrpc.client.ServerProxy('http://localhost:%s' % local_port)    

    arr=take_picture()
    print(arr.shape)
    


# In[ ]:




