# a=int(input("Enter your age "))
# print("Your age is:",a)

#conditional operator
#>,<,>=,<=,==,!=

# print(a>18)
# print(a<18)
# print(a==18)
# print(a!=18)

# if(a>18):

#     print("you can drive")
# else:
#     print("you can't drive")
# print("no") #identation error    

#Else-if statement

apple_price=10
budget=200

# if(budget-apple_price>50):
#  print("add 1 kg apple to list")

# else:
#    print("Alexa do not buy apple")

#elif statement
# 
# num=int(input("Enter the value"))
# if(num<0):
#     print("number is negative:")
# elif(num==0):
#     print("Number is zero:")
# elif(num==888):
#     print("Number is special")
# else:
#     print("Number is positive")

#     print("jai shree ram")

#nested-if statement
num=int(input("Enter the vslue of num "))
if(num<0):
    print("num is negative")
elif (num>0):
    if(num<=10):
      print("number is between 0-10")
    elif(num>10 and num <=20):
      print("number is between 11-20")
    else:
      print("number is greater than 20")
else:
    print("number is zero") 
