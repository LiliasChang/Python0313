
# coding: utf-8

# In[1]:


name_table = {'綠⾊色': 1, '紅⾊色': 2}


# In[2]:


print(name_table)


# In[3]:


new_name = name_table.setdefault('橘⾊色', 12)


# In[4]:


new_name


# In[5]:


name_table


# In[9]:


from collections import defaultdict
name_table2 = defaultdict(int)


# In[10]:


name_table2


# In[11]:


name_table2['青⾊色']


# In[12]:


name_table2


# In[13]:


name_table2['橘⾊色']


# In[14]:


name_table2


# In[16]:


food_count = defaultdict(int)


# In[21]:


for food in ['spam','spam','eggs','spam']:
    food_count[food]+=1


# In[22]:


food_count


# In[27]:


from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)


# In[28]:


breakfast_counter


# In[29]:


breakfast_counter.most_common()


# In[30]:


breakfast_counter.most_common(1)


# In[31]:


import itertools
for item in itertools.chain([100, 102], ['⽂文字1', '⽂文字2']):
    print(item)


# In[33]:


import itertools
for item in itertools.cycle([100, 102]):
    print(item)


# In[34]:


import itertools
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

