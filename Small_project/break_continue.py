#Break statement

# for i in range(11):
#     if(i==10):
#              break
#     print("5 X",i+1,"=",5*(i+1))
    
   
# print("we exit from the loop")

#difference between break statement and continue statment
# for i in range(12):
#     if(i==10):
#               print("Skip the iteration")
#               continue
#     print("5 X",i,"=",5*i)
    
   
# print("we exit from the loop")

#continue statement
# for i in [2,3,4,6,8,0]:
#     if(i%2!=0):
#         continue
#     print(i)  

#emmulating do while loop
# i=0
# while True:
#     print(i)
#     i=i+1
#     if(i%10==0): 
#         break

#example2 of emulating do while loop
while True:
    number=int(input("Enter the positive number:"))
    print(number)
    if not number>0:
        break