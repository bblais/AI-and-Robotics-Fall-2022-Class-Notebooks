#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def watch_new_files(dirname,verbose=False):
    import glob
    import os
    import time
    
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


# In[ ]:


def scp(local,remote,user_hostname=None,passwd=None,debug=False):
    import os
    assert not passwd is None
    assert not user_hostname is None
    assert '@' in user_hostname
    cmd="sshpass -p %s scp -o StrictHostKeyChecking=no '%s' %s:'%s'" % (passwd,local,user_hostname,remote)
    print(cmd)
    if not debug:
        os.system(cmd)


# In[ ]:


def scp(local,remote,user_hostname=None,debug=False):
    import os
    assert not passwd is None
    assert not user_hostname is None
    assert '@' in user_hostname
    cmd="scp '%s' %s:'%s'" % (local,user_hostname,remote)
    print(cmd)
    if not debug:
        os.system(cmd)


# In[ ]:





# In[ ]:


for filename in watch_new_files('/Volumes/GoogleDrive/My Drive/Robot_Phone_Pictures',verbose=True):
    scp(filename,
        'python/picture.jpg',  # filename on robot
        'pi@dex.local','password',
       debug=False)


# In[ ]:


import subprocess
command = ["scp", '/Volumes/GoogleDrive/My Drive/Robot_Phone_Pictures/IMG_3591.JPG','pi@dex.local:python/']
output,error  = subprocess.Popen(
                command, universal_newlines=True,
                stdout=subprocess.PIPE,  
                stderr=subprocess.PIPE).communicate()


# In[ ]:


output,error


# In[ ]:


import subprocess

command = ["scp", '/Volumes/GoogleDrive/My Drive/Robot_Phone_Pictures/IMG_3591.JPG','pi@dex.local:python/']
# Enter "google.com; cat /etc/passwd", without quotes.
subprocess.run(command, shell=True)


# In[ ]:




