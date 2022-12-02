#!/usr/bin/env python
# coding: utf-8

# In[20]:


def watch_new_files(dirname,verbose=False):
    import glob
    import os
    import time
    assert os.path.isdir(dirname)
    
    first_time=True
    old_files=[]
    if verbose:
        print("Watching ",dirname)
    try:
        while True:
            files = list(filter(os.path.isfile, glob.glob(os.path.join(dirname,"*"))))
            files.sort(key=lambda x: os.path.getmtime(x))

            if first_time:
                pass
            elif len(files)!=len(old_files):
                yield files[-1]

            first_time=False
            old_files=files
            if verbose:
                print(".",end="")


            time.sleep(1)
    
    except KeyboardInterrupt:
        if verbose:
            print("done.")


# In[21]:


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


# In[23]:


passwd_=getpass("Enter password:")  # robot password


# In[22]:


for filename in watch_new_files('G:/My Drive/Robot_Phone_Pictures',verbose=True):
    scp(filename,'pi@10.2.2.30','python/picture.jpg')


# In[ ]:




