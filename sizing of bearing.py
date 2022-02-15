#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Sizing of bearings 
#Calculation of the bearing means to find (select) the one able, 
# with certain reliability, to achieve its purpose.
# The required size of the bearing for a particular bearing position is determined based on the type of bearing 
# and its capacity, present loads, designed life span and operational safety.
# Dynamic  and static $ bearing capacity are used as capacity measures for their sizing.
# Dynamic capacity is a capacity criterion for the selection of dynamic capacity bearings,
# or bearings with rotation under load. It is determined depending on the bearing life span, based on the expression:
print('''Bearing Size Calculater\n''')
print("\n")
print("\n")
#here we are going to calculate the Sizings of the bearings

print('''The General Formula is : C = F*((fL*ft)/fn) \n
Where :  
F= Equivalent dynamic bearing load\n
fL= Factor of durability\n
ft= Factor of temperature\n
fn= Factor of number of revolutions''')

print('''To Calculate the Force Please input the following:''')
f = float(input("Enter the Equivalent dynamic bearing load F : "))
fl = float(input("Enter the Factor of durability fL : "))
ft = float(input("Enter the Factor of temperature ft: "))
fn = float(input("Enter the Factor of number of revolutions fn: "))
c = f*((fl*ft)/fn)
print("The size of bearing is: ",c)


# In[ ]:




