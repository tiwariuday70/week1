#!/usr/bin/env python
# coding: utf-8

# In[2]:


#dictionaries
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook) #this will prints the numbers according to related person in a set 


# In[3]:


phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook) #this will prints the numbers according to related person in a set 


# In[4]:


phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))#this will print the phone numbers of persons in a sentence form in a order
    


# In[5]:


phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)#prints the numbers with related to specefic person in a set and deletes phone number with name john


# In[6]:


phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)# prints the number by deleting name john


# In[7]:


phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook["Jake"] = 938273443 
del phonebook["Jill"] 

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")#prints jake is listed in the phonebook
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")#prints jill is not in phonebook


# In[ ]:




