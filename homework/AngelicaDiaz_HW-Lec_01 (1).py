#!/usr/bin/env python
# coding: utf-8

# In[1]:


R = 1.097e-2
for m in [1,2,3]: 
    if m == 1: print("Lyman Series")
    if m == 2: print("Balmer Series")
    if m == 3: print("Paschen Series")
    print ("Series for m =", m)
    for k in [1,2,3,4,5]:
        n = m + k
        invlambda = R*(1/m**2 - 1/n**2)
        print("n =", n)
        print ("Wavelength =", 1/invlambda, "nm")
        if k == 5: print()  


# In[ ]:




