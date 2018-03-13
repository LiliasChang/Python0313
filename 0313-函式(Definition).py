
# coding: utf-8

# In[1]:


def do_nothing():
    pass


# In[2]:


do_nothing()


# In[3]:


def add_args(arg1,arg2):
    print(arg1+arg2)


# In[4]:


add_args(1,2)


# In[7]:


def iron_man_color(arg_color):
    if arg_color == "紅色":
        return("鋼鐵人是紅色的")
    elif arg_color == "綠色":
        return("鋼鐵人其實也可以參考浩克")
    elif arg_color == "藍色":    
        return("鋼鐵人變成小精靈也不錯")
    else:
        return("好像沒這種顏色",arg_color) 


# In[8]:


iron_man_color("紅色")


# In[9]:


iron_man_color("黑色")


# In[10]:


def ans():
    print(42)


# In[11]:


ans()


# In[13]:


x =ans()


# In[15]:


print(x)


# In[19]:


def add_arg(arg1,arg2):
    print(arg1+arg2)


# In[20]:


def run_with_args(func,arg1,arg2):
    func(arg1,arg2)


# In[21]:


run_with_args(add_arg,1,2)


# In[25]:


def run_with_args_new(func,*args):
    return func(*args)


# In[26]:


run_with_args_new(add_arg,1,2,3,4,5,6)


# In[27]:


def run_with_args_new2(func,*args):
    return sum(args)


# In[28]:


run_with_args_new2(add_arg,1,2,3,4,5,6)


# In[38]:


def cowsay(saying):
    def inner(quote):
        return "cowsay:'%s'"%quote
    return inner(saying)


# In[39]:


cowsay("哞")


# In[43]:


def cowsay2(saying):
    def inner():
        return "cowsay:'%s'"%saying
    return inner


# In[44]:


cowsay2("哞哞")


# In[46]:


a = cowsay2("哞哞")
a()


# In[51]:


def gen_power(base):
    def power(exp):
        return base + exp
    return power


# In[52]:


b = gen_power(10)
b(3)


# In[53]:


c = gen_power(20)
c(2)


# In[54]:


def edit_story(words,func):
    for word in words:
        print(func(word))


# In[55]:


A = ['hello','hi','hey','oops']


# In[57]:


def cap(word):
    return word.capitalize() + '!'


# In[58]:


edit_story(A,cap)


# In[59]:


edit_story(A, lambda word:
word.capitalize() + '!')


# In[60]:


def document_it(func):
    def new_function(*args, **kwargs):
        print('執⾏行行函式',func.__name__)
        print('參參數位置', args)
        print('關鍵字參參數', kwargs)
        result = func(*args, **kwargs)
        print('結果:',result)
        return result
    return new_function


# In[61]:


def add_ints(a,b):
    return a+b


# In[62]:


add_ints(3, 5)


# In[63]:


@document_it
def add_ints(a,b):
    return a+b


# In[64]:


add_ints(3, 5)


# In[65]:


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        print('New結果:',result)
        return result * result
    return new_function


# In[66]:


@document_it
@square_it
def add_ints(a,b):
    return a+b


# In[67]:


add_ints(3, 5)

