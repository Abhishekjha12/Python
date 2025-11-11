# x=0b11011000
# print(x)
# print(type(x))
# y=0o123
# print(y)
# z=0x19A
# print(z)
# print(abs(-3.5))
# str1="shakespeare"
# sub1=str1[0:5]
# sub2=str1[0:6:2]
# a=10
# b=5
# a=b
# print(a)

# n=int(input("Enter the number"))
# h=n//2
# while h>=2:
#     if n%h==0:
#         print("Composite\n")
#         break
#     h=h-1
# else:
#     print("number is prime\n")

# n=int(input("Enter any number"))
# h=n//2
# while h>=2:
#     if n%h==0:
#         print("Composite\n")
#         break
#     h=h-1
# else:
#     print("number is prime\n") 
# S="COMPUTER"
# T="computer"
# I='C'
# print(I in S)
# print('A' in S)
# print('S' is T)#memory address are different

# for j in range(-5,5,2):
#     print(j)
# for j in range(10):
#  print(j)    

# S="jupyter"
# T="12345"
# for j in S:
#    for k in T:
#       print(j,k)

#
# 
# l1=[1,2,3,4,5]
# l2=[5,4,3,2,1]
# l3=l1+l2
# print(l3)
# l4=l1
# print(id(l4))
# print(id(l1))
# l1=l2
# Res=l1 is l2
# print(Res)

# A=[1,2,9,9,5]
# B=[1,2,9,6,7]
# C=[33,1]
# res1=A<B
# print(res1)
# print(max(A))
# print(min(B))
# print(min(C))
# print(max(C))
# l1=[1,3,[11,13,15,[17,19],21],5,7]
# print(l1[0:3])

# 
# student_list=["Aditya","shradha","adi","ragini"]
# NewList=[Name for Name in student_list if Name.startswith('s')]
# print(NewList)

# stringNew=["*" if letter in 'aeiouAEIOU' else letter for letter in "Education"]
# print(stringNew)
# List=[[1,2,3],[4,5,6],[7,8,9]]
# L=[n for row in List for n in row]
# print(L)
# List_p1=[i*j for i in range(1,5) for j in range(1,5)]
# List_p2=[[i*j for i in range(1,5)] for j in range(1,5)]
# print(List_p1)
# print(List_p2)

# a={(n,n*n) for n in range(1,10)}
# print(a)

T1=1,2,3
T2=4,5,6
T3=7,8,9
T=T1,T2,T3
# print(T)
# print(T[2][1])
T4=10,11,T1
print(T4)