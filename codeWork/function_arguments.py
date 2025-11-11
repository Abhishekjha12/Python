# def average(a,b):
#         print("The average is",(a+b)/2)

# average(4,6)

# default argument    
# def average(a=4,b=6):

#     print("The average is",(a+b)/2)
# average(b=5)

# keyword argument
# def average(a=9,b=1):
#     print("The average is",(a+b)/2)
# average(b=9,a=21)

# required ar;gument
# def average(a,b,c=1):
#     print("The average is ",(a+b+c)/2)
# average(5,6)    

#example2
# def name(fname, mname, lname):
#     print("Hello,",fname,mname,lname)

# name("Peter","Quill","nice")      

# variable-length arguments
def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    # print("Average is:",sum/len(numbers))
    # return sum/len(numbers)
# average(5,6)

c=average(5,6,7,1)
print(c)
# #arbitary arguments:
# def name(*name):
#     print("Hello",name[0],name[1],name[2])
# name("James","Buchanan","Barnes")    