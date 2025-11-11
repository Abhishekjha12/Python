#Manipulating tuple:
#no direct way

countries=("spain","italy","india","england","Germany")
# temp=list(countries)
# temp.append("Russia") #add item
# temp.pop(3) #remove item at index 3
# temp[2]="Finland" #change the item
# countries=tuple(temp)
# print(countries)

#we can directly concatenate tuple into list
# countries=("pakistan","afghanistan","Bangladesh","sri lanka")
# countries2=("vietnam","India","china")
# southEastAsia=countries+countries2
# print(southEastAsia)

#count method: tells about count the occurences of an element
tuple=(0,1,2,3,2,3,1,3,2,3 )
# res=tuple.count(3)
# print('count of 3 in tuple is:',res)

#index method: give first occurenece of an element from the tuple
# res=tuple.index(1)
# print('the first occurence 1 is',res)
#we can also specify the range between which we want the occcurence to be checked
# ret=tuple.index(3,4,8)
# print("count of 3 is",ret)
res=len(tuple)
print(res)
# tuples are inmmutatble
