#!/usr/bin/env python
# coding: utf-8

# In[2]:


#ranges


# In[3]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[5]:


for nun in range(0,10):
    print(nun)


# In[6]:


list(range(0,10))


# In[7]:


#enumerate


# In[8]:


index_count = 0
for letter in 'abcde':
    print('at index{}the letter is {}'.format (index_count,letter))
    index_count +=1


# In[9]:


word = 'abcde'
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')


# In[10]:


#zip function  


# In[11]:


mylist1 = ['a','b','c']
mylist2 = [1,2,3]
for item in zip(mylist,mylist2):
    print(11)
    print(12)


# In[14]:


mylist1 = ['a','b','c']
mylist2 = [1,2,3,4,5]
mylist3 = [11,22,33]
for 11,12,13 in zip(mylist1,mylist2,mylist3):
    print(11)
    print(12)
    print(13)


# In[15]:


#in keyboard 


# In[16]:


'x' in [1,2,3]


# In[18]:


'a' in 'wonder la'


# In[22]:


d = {'mykey':345}


# In[23]:


345 in d.values()


# In[24]:


#min,max


# In[25]:


mylist = [10,20,30,40,50,60]
min(mylist)


# In[26]:


max(mylist)


# In[1]:


#random library


# In[3]:


from random import shuffle
mylist = [1,2,3,4,5,6,7,8]
shuffle(mylist)
rd1 = mylist


# In[4]:


rd1


# In[5]:


from random import randint
randint(0,10)


# In[6]:


randint(0,100)


# In[8]:


my_num = randint(0,50)


# In[9]:


my_num


# In[10]:


#input()


# In[12]:


input('enter a number here')


# In[14]:


input('what is your favourite color?')


# In[15]:


int(input('enter your favourite no'))


# 

# In[16]:


result = int(input('enter your favourite no'))


# In[17]:


result


# In[18]:


type(result)


# In[19]:


number = float(input('enter 1st number'))
number_two = float(input('enter second number'))
result = number + number_two
print(result)


# In[20]:


#input()


# In[21]:


input('enter a name here')


# In[31]:


result = '2'
print(result)


# In[32]:


result


# In[33]:


#output()


# In[35]:


my_list = [1,2,3,4,5,6,]


# In[36]:


my_list


# In[40]:


from random import shuffle
mylist = [1,2,3,4,5,6,7,8]
mylist2 =[2,4,5,6,7,8]
shuffle(mylist)
rd1 = mylist
rd2 = mylist2


# In[41]:


rd2


# In[42]:


rd1


# In[44]:


shop = 'vialoop'
if shop == 'kewal':
    print('he will buy apples')
elif shop == 'vialoop':
    print('he will buy maangos')

else:
    print('he will eat it in shop')
    


# In[45]:


#list compreshension in python


# In[ ]:




