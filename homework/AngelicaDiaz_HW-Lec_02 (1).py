#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("To find the multiplicity (Omega) of any (N,q): ")
print("Let N be the number of oscillators")
print("Let q be the energy levels")
def factorial(N):
#Can also use "from math import factorial"
    if N == 0 or N == 1:
        return 1
    else: 
        total = 1
        for i in range(1,N+1):
            total *= i
        return total     

def Multiplicity(N,q):
    return factorial(q+N-1)/(factorial(q)*factorial(N-1))
    
N=int(input("Type the number of oscillators, N: "))
q=int(input("Type a value for q: "))
    
print ('The multiplicity is',  Multiplicity(N,q)) 


# In[ ]:




