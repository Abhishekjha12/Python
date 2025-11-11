#set and tuple
# s="Anuj"
# s[0]='c'
# a=('A','b','h','i') this is tuple
# a[0]='c'

# print(a)

#set
# a={1,2,4,6,4,6,1}
# for element in a:  #iteration in set
#     print(element*2)
# print(a)
# print(a[0]) indexing is not defined in set

#dictionary
#key and value pairs are stored
# dict={key:"value"} #format of dictionary
#for example

# dict={1:'mango',2:"lassi",3:"sweet"}
# print(dict)

#for example we want to store the marks of students in a class
# marks={"kuchhu":34,"pauwa":56,"nagu":100,"jha ji":10}
# print(marks)
#key and value can be of same class and different class

#to access any partiular value
# print(marks["nagu"],marks["jha ji"])
# marks["rohit"]=99
# marks["kuchhu"]=45
# print(marks)

#iteration in dictionary

# squares={1:1,2:9,3:8}
# for i in squares:
#     print(i,squares[i])

#updating in dictionary
# by modifying the existing key value pair or by merging another dictionary to an existing one
# we can add new items or change the value of existing items using assignment operator
# if the key is already present, value gets updated,else a new key: value pair is added to the dictionary

#Python functions
#group of related statement that perform a specific task

#categories of function
# 1. built-in: int() float() min() max() len() etc
# 2.module: file containing functions and variables in separated files. A module is 
# simply a file that contains python code
# important module:
# math
# random
# string

#for example
# import math as m
# print(m.pi)
# print(m.sin(45))

#to import specific function from a module
# from math import cos
# print(cos(3.14))
#to import multiple specific function from a module
# from math import cos,sin,pi
# print(cos(3.14))
# print(sin(45))
# print(pi)

#to import all entire function
# use *
# for exmaple
# from math import *
# print(sin(45))
# print(cos(45))
# print(tan(45))

#USER defined functions
#syntax: def
# def_function_name(parameter)
    #   """DOCSTRING"""
# statement(s)
#for example
# def greet():
#     print("Good morning,Anuj") #interpreter this function but not execute it
# greet()  #function call  
# greet()  #function call  

#to input from user in a function call
# def greet(name,dish='pasta'):
#     print("Good morning",name)
#     print('please eat',dish)

# greet('shivam')

#returning the function
# def sum_of_list(a):
#     print('calculating...')
#     return sum(a)

# marks=[45,15,23,56,99] #marks stored in marks
# sum_of_marks=sum_of_list(marks) #function is called and sum of list is returned
# print('my sum of marks',sum_of_marks)

#Write a program that take names from a list and greet them
# def greet(names):
#  for name in names:
#   print("Hello")

# names=['Anuj','Nagu','Shubham']
# greet(names)

#file handling
# File= file is name location on disk to store related information.
#it is used to permanently store data in a non volatile memory(e.g hard disk)
# in pyhton a file operation place in the following order
#1. open file
# 2. read or write 
#3. close the file

# f=open("filehandling.txt.txt",'r')
# for line in f:
#     print(line)
# a=[]
# a[4]
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

with open("C:\Users\Abhishek Jha\Dropbox\PC\Desktop\python_programming\filehandling.txt.txt")as f:
    # for line in f:
    #     print(line)
    print(f.read(10))    
    f.seek(0) 