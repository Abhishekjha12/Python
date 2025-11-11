#tuples once made cant be changed
# tup=(1,5,6)
# print(type(tup),tup)
tup=(1,2,3,4,5,"green",True)

#it is nesecessary to give a comman 
#so that it ease python to understand tha
#whether we r writing a value or creating a new tuple
print(type(tup),tup)  
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[5])

#positive and negative indexing are same in tuple
#like the list

#conditioning
if 342 in tup:
    print("yes")
else:
    print("no")

#tuple slicing
tup2=tup[1:4]
print(tup2)
#tuples are immutable