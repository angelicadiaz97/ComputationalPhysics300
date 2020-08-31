#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("To find the multiplicity (Omega) of any (N,q): ")
print("Let N be the number of oscillators")
print("Let q be the energy levels")
def factor(N):
    if N == 0 or N == 1:
        return 1
    else: 
        total = 1
        for i in range(2,N+1):
            total *= i
        return total     

def Multiplicity(N,q):
    return factor(q+N-1)/(factor(q)*factor(N-1))
    
N=int(input("Type the number of oscillators, N: "))
q=int(input("Type a value for q: "))
    
print ('The multiplicity is',  Multiplicity(N,q))


# In[ ]:





# In[ ]:




