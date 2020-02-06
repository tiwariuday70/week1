#!/usr/bin/env python
# coding: utf-8

# In[4]:


print("hello world")#prints hello world


# In[5]:


#var and types
myint=7
print(myint)#integer type


# In[6]:


myfloat=7.0#float type
print(myfloat)


# In[8]:


#string
mystring='hello'
print(mystring)#printing string


# In[9]:


a="dont worry about this"
print(a)


# In[10]:


one=1
two=2
three=one+two
print(three)
hello="hello"
world="world"
helloworld=hello+""+world#prints using operators in strings
print(helloworld)


# In[11]:


a,b=3,4
print(a,b)#prints multiple variable


# In[12]:


mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)#crate string
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)#create floating point number
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)#create integer


# In[14]:


#Arthemetic operators
number=2+1*3/4.0 #using different arethemetic operators
print(number)


# In[15]:


rem=11%3
print(rem)#using modulus will gives remainder


# In[18]:


square=4**2
print(square)#to print square opf 4
cube=2**3
print(cube)#to print cube of 2


# In[19]:


helloworld = "hello" + " " + "world"
print(helloworld)#using operator with string


# In[20]:


lotsofhello='hello'*10
print(lotsofhello)#prints hello ten times in same line


# In[23]:


even_numbers=[2,4,6,8]
odd_numbers=[1,3,5,7]
all_numbers=even_numbers+odd_numbers#this will join odd and even numbers
print(all_numbers)


# In[ ]:




