#!/usr/bin/env python
# coding: utf-8

# In[5]:


def watch(filename):
    import os,time
    print("Watching ",filename,':')
    if not os.path.exists(filename):
        use_exist=True
        stamp=os.path.exists(filename)
    else:
        use_exist=False
        stamp = os.stat(filename).st_mtime
    
    while True:
        if use_exist:
            new_stamp=os.path.exists(filename)
        else:
            new_stamp=os.stat(filename).st_mtime
        print(".",end="")
        if new_stamp!=stamp:
            break
        time.sleep(0.5)
        
    print("done.")


# In[6]:


watch('picture.jpg')


# In[ ]:




