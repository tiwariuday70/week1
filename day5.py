#!/usr/bin/env python
# coding: utf-8

# In[1]:


### basic string operations
astring = "Hello world!"
print(astring[3:7:2])#prints the string from 3to6 by skipping one character in between them 


# In[2]:


astring = "Hello world!"
print(astring[3:7])#prints string from 3 to 6
print(astring[3:7:1])#prints string from 3 to 6 


# In[3]:


astring = "Hello world!"
print(astring[::-1])#this will reverse the string


# In[4]:


astring = "Hello world!"
print(astring.upper())#print the string in uppercase
print(astring.lower())#print the string in lowercase


# In[6]:


astring = "Hello world!"
print(astring.startswith("Hello"))#this string checks whether string starts with hello and diplay true 
print(astring.endswith("asdfasdfasdf"))#this string check whether it ends with asdfasdfasdf and diplay false


# In[12]:


astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)#splits the string into bunch in a list


# In[13]:


s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))


# In[14]:


#conditions 
x = 2
print(x == 2) # displays true
print(x == 3) #displays false
print(x < 3) # displays true


# In[15]:


name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")#displays Your name is john, and you are also 23 years old as condition satisfies

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")#displays Your name is either john or nick as it satisfies one condition


# In[16]:


name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")#displays Your name is either name or rick because list satisfies the name ie.john


# In[18]:


x = 2
if x == 2:
    print("x equals two!")#displays x equals two! as it is true
else:
    print("x does not equal to two.")#its false so donot display this


# In[19]:


x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints true as x and y has same value in list
print(x is y) # Prints false as is doesnot match the value like ==


# In[20]:


print(not False) #print true as it gives true meaning in sense
print((not False) == (False)) # prints false 


# In[21]:


number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")#since number is less than 1 so print 15

if first_array:
    print("2")#there is 2 in first_array so print 2

if len(second_array) == 2:
    print("3")#prints 3 as there is two in the second_array list

if len(first_array) + len(second_array) == 5:
    print("4")#prints 5 as sum of length of first_array and second_array is 5
if first_array and first_array[0] == 1:
    print("5")#prints 5 as index[0] of first and second array is 1


# In[22]:


#lists examples
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1 as indexing of 0 is given as 1
print(mylist[1]) # prints 2 as indexing of 1 is given as 2
print(mylist[2]) # prints 3 as indexing of 2 is given as 3

for x in mylist:
    print(x)#prints the numbers from list 


# In[27]:


mylist = [1,2,3]
print(mylist[10])#wrong as list index is out of range


# In[28]:


#correction
mylist = [1,2,3]
print(mylist[2])


# In[29]:


numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)#prints the numbers 1,2,3 in the list
print(strings)#prints the strings hello and world in a list
print("The second name on the names list is %s" % second_name)#prints the second name on the name list is eric and indexing is 1


# In[30]:


#loops examples
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)#prints the numbers from list


# In[31]:


# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)#prints numbers less than 5 starting from 0

# Prints out 3,4,5
for x in range(3, 6):
    print(x)#prints numbers from 3 to 5

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)# prints numbers from 3 to 7 skiping one character


# In[32]:


count = 0
while count < 5:
    print(count)# this will gives the numbers starting from 0 and less than 5 
    count += 1  # this will increase number by 1 


# In[33]:


count = 0
while True:
    print(count)#prints numbers from 0 by incresing 1 
    count += 1
    if count >= 5:#will hult if count will be >=5
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)#this will print the result by skipping the current block 


# In[34]:


count=0
while(count<5):
    print(count)#this will print numbrs from 0 to 4
    count +=1
else:
    print("count value reached %d" %(count))#print count value reached 5

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break#this will hult the result if i%5==0
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")


# In[36]:


numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:#hults if numbers== 237
        break

    if number % 2 == 1:#prints the result by skiping the current block
        continue

    print(number)#print numbers by hult if numbers==237


# In[ ]:




