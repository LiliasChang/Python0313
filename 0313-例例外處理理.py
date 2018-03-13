
# coding: utf-8

# In[1]:


x=[1,2,3,4]
x[6]


# In[2]:


p = 6


# In[4]:


try:
    x[p]
except:
    print("輸入錯誤",p,"重新輸入(0~3)")

