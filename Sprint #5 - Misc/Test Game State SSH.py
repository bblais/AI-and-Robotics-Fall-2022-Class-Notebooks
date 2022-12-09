#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *


# In[2]:


from getpass import getpass
def scp(local,user_hostname,remote):
    global passwd_
    
    import os,shutil
    assert os.name=='nt'  # only works on windows
    assert shutil.which('pscp')
    
    assert '@' in user_hostname
    cmd='pscp -pw "%s" "%s" %s:"%s"' % (passwd_,local,user_hostname,remote)
    cmd_='pscp -pw "%s" "%s" %s:"%s"' % ('*'*len(passwd_),local,user_hostname,remote)
    print(cmd_)
    os.system(cmd)


# In[3]:


passwd_=getpass("Enter password:")  # robot password


# In[ ]:




