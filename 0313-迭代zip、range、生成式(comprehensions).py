
# coding: utf-8

# In[1]:


e = "book","apple","computer"
c='書','蘋果',"電腦"


# In[2]:


type(c)


# In[3]:


list(zip(e,c))


# In[4]:


dict(zip(e,c))


# In[5]:


for x in range(1,10):
    print(x)


# In[7]:


list(range(1,10))


# In[8]:


tuple(range(1,10))


# In[9]:


tuple(range(1,10,2))


# In[10]:


range(1,10)


# In[12]:


number_list = list(range(1,6))
number_list


# In[14]:


number_list2=[]
number_list2.append(1)
number_list2.append(2)
number_list2.append(3)
number_list2.append(4)
number_list2.append(5)
number_list2


# In[15]:


number_list3 =[]
for n in range(1,6):
    number_list3.append(n)
number_list3


# In[16]:


number_list4 = [n for n in range(1,6)]
number_list4


# In[17]:


[n - 1 for n in range(1,6)]


# In[19]:


number_list4 = [n + 1 for n in range(0,5)]
number_list4


# In[21]:


a_list = []
for number in range(1,6):
    if number % 2 == 1:
        a_list.append(number)

a_list


# In[22]:


[n  for n in range(1,6) if n%2 == 1]


# In[24]:


x = range(1,10)
y = range(1,10)
for i in x:
    for j in y:
        print(str(i) +"*" +str(j) + " = " + str(i *j))


# In[25]:


for i in range(1,10):
    for j in range(1,10):
        print(str(i) +"*" +str(j) + " = " + str(i *j))


# In[26]:


for i in range(1,10):
    for j in range(1,10):
        print(i,"*",j," = ",i *j)


# In[38]:


[(x,'*',y,'=',x *y )for x in range(1,10) for y in range(1,10) ]

