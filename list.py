# marks=[3,5,6,"Abhi",True]
# print(marks)
# print(type(marks))
# print(marks[0]) 
# print(marks[1])
# print(marks[2])

# #list can include different data types
# list=[2,3,4,"Abhi",True]
# print(list)
# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# print(list[4]) 


#negative indexing
# print(marks[-3])
# print(marks[len(marks)-3]) #positive index
# print(marks[5-3]) #positive index
# print(marks[2])#positive index

#to check whether 7 is in our list or not

# if 7 in marks:
#     print("yes")
# else:
#     print("no")
# if "Abhi" in marks:
#     print("yes")
# else:
#     print("no")

#same thing apply to string as well
#for example
# if "bh" in "Abhi":
#     print("yes")
# else:
#     print("no")

#other way to print an entire string
# print(marks[:])
# #slicing in list
# print(marks[1:4])
# #jump index
# print(marks[1:4:2])

# strip=[1,2,3,4,5,6,"jha ji",True,8,9,10,11,12]
# print(strip[1:-8])
# print(strip[1:8:4]) #here we are performing jump indexing by margin of 3

#List compreshension
lst=[i for i in range(4)]
print(lst)
lst=[i for i in range(10) if i%2==0]
print(lst)
