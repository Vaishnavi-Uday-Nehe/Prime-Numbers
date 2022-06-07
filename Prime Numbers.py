#!/usr/bin/env python
# coding: utf-8

# In[14]:


n = 101

if n>1:  
    for i in range(2, n): #starting from 2 to the given integer 101
        if n%i == 0:
            print(n,"is not a prime number")
            break #break is necessary as the result will be printed only once 
        else:
            print(n,"is a prime number")
            break
else: #if n is less than 1
    print(n,"is not a prime number")
    
#CodeByVaishnaviUdayNehe


# In[ ]:




