#!/usr/bin/env python
# coding: utf-8

# In[2]:


name = "ram"
age = 23
print("%s is %d years old." % (name, age))#prints ram is 23 years old


# In[3]:


mylist = [1,2,3,4,5]
print("A list: %s" % mylist) #prints A list:[1,2,3,4,5]


# In[4]:


data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string % data)#this will give error


# In[5]:


#the right soln is
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)#this will give  hello john doe.Your current balance is $53.44


# In[6]:


#the basic strfing operator
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))#counts the total  no of letters 


# In[1]:


#string formatting
name = "uday"
print("Hello, %s!" % name)#prints the name hello uday!


# In[7]:


astring = "Hello world!"
print(astring.count("l"))#counts the total no of l 


# In[8]:


astring = "Hello world!"
print(astring.index("o"))#prints the index value of o


# In[9]:


astring = "Hello world!"
print(astring[3:7])#prints the indexing string that starts with 3 and less than 7 


# In[ ]:




