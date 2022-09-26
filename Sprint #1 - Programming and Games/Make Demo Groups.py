#!/usr/bin/env python
# coding: utf-8

# In[1]:


names="""
Darya
Mia
Michael
Gianni
Griffin
Brad
Katie
Adam
Anxhela
Natalia
Jason
Nathan
Trey
Chidi
Jess
Dave
Ethan
Reese
Oscar
Will
""".strip().split()


# In[2]:


names


# In[3]:


from random import choice


# In[4]:


names_orig=names.copy()


# In[5]:


names=names_orig.copy()
pairs=[]
extra=None
while names:
    name1=choice(names)
    names.remove(name1)
    
    try:
        name2=choice(names)
        names.remove(name2)
    except IndexError:
        extra=name1
        continue
    
    pairs.append( [name1,name2])


# In[6]:


pairs


# In[7]:


extra


# In[8]:


found_duplicate=True
while found_duplicate:
    print("# Demo Pairs")
    extra=None
    found_duplicate=False
    all_pairs=[]
    for i in range(3):
        names=names_orig.copy()
        pairs=[]

        while names:
            
            if extra:
                name1=extra
                extra=None
            else:
                name1=choice(names)
                
            names.remove(name1)

            try:
                name2=choice(names)
                names.remove(name2)
            except IndexError:
                extra=name1
                continue

            if name2<name1:
                name1,name2=name2,name1
                
            pairs.append( (name1,name2) )
            
        for p in pairs:
            print("- ",p[0]," - ",p[1])
            if all_pairs:
                if p in all_pairs[-1]:
                    print(p,"duplicate")
                    found_duplicate=True
            

        print("\n------\n")
        all_pairs.append(pairs)
                        
                        


# # Demo Pairs
# -  Reese  -  Will
# -  Gianni  -  Jason
# -  Griffin  -  Oscar
# -  Adam  -  Nathan
# -  Chidi  -  Mia
# -  Brad  -  Katie
# -  Darya  -  Jess
# -  Ethan  -  Michael
# -  Anxhela  -  Trey
# -  Dave  -  Natalia
# 
# ------
# 
# -  Mia  -  Reese
# -  Adam  -  Gianni
# -  Chidi  -  Trey
# -  Katie  -  Oscar
# -  Jason  -  Michael
# -  Darya  -  Dave
# -  Brad  -  Jess
# -  Griffin  -  Nathan
# -  Anxhela  -  Will
# -  Ethan  -  Natalia
# 
# ------
# 
# -  Jess  -  Natalia
# -  Anxhela  -  Michael
# -  Gianni  -  Trey
# -  Darya  -  Katie
# -  Chidi  -  Jason
# -  Brad  -  Mia
# -  Oscar  -  Will
# -  Dave  -  Nathan
# -  Adam  -  Reese
# -  Ethan  -  Griffin
# 
# ------
# 

# In[9]:


name1


# In[10]:


name2


# In[ ]:




