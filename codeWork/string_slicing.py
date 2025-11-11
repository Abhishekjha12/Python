#strig slicing= it is done by putting : between the indices
#and the character between those indices is printed,except the last indices
#as 1 less indices is printed

#name="shubham,mukesh"
#print(name[2:8])

#string length using len function
#string lenght can take any name but should have len function in it without spaces
fruit="mango"
mangolen1=len(fruit)
print(mangolen1)
#print(fruit[0:4]) #including 0 not 4
#print(fruit[1:4])#including 1 not 4
#negative slicing
#print(fruit[0:-3])
#print(fruit[0:len(fruit)-3])
print(fruit[-1:len(fruit)-3])
print(fruit[-3:-1])