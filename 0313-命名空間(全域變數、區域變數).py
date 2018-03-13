
# coding: utf-8

# In[1]:


a = 'pig'


# In[2]:


def print_global():
    print('全域變數',a)


# In[3]:


print_global()


# In[4]:


def s():
    print(45)


# In[5]:


x =s()
print(x)


# In[6]:


a


# In[7]:


def change_local():
    a = 'dog'
    print(a)


# In[9]:


change_local()


# In[10]:


a


# In[11]:


def change_local():
    global a
    a = 'dog'
    print(a)


# In[12]:


change_local()


# In[13]:


a


# In[14]:


print('全域變數',globals())


# In[15]:


del a
print('全域變數',globals())

