# def display_data(p,q,r):
#     print(p**2)
#     print(round(q,2))
#     print(r.title())
# display_data(10,3.142876," i love you")

# def sum_cubes(n1,n2,n3):
#     sum3=n1**3+n2**3+n3**3
#     return sum3
# s=sum_cubes(1,2,3)
# print("The result is",s)

# def display_data(number,pi_n,cringe):
#     print(number**2)
#     print(cringe.title())
#     print(round(pi_n,2))
# display_data(cringe="i love you",number=10,pi_n=3.142876)

# variable positional argument
# def sum_cubes(*var_arg):
#     sum3=0
#     for j in var_arg:
#         sum3+=j**3
#     return sum3
# s1=sum_cubes(1,2) #added value then cubed
# print("The first result is",s1)
# s2=sum_cubes(1,2,3,4) #added value then cubed
# print("The secod result is",s2)    

#to find integer quotient and remainder of two number
# def div_mod(*var_arg):
#     q=var_arg[0]//var_arg[1]
#     r=var_arg[0]%var_arg[1]
#     return q,r
# n1=int(input("Enter the dividend\n"))
# n2=int(input("Enter the divisor\n"))
# T=div_mod(n1,n2)
# print("The quotient and remainder are",T)

#variable keyword argument

# def div_mod(**kw_args):
#     q=kw_args['dividend']//kw_args['divisor']
#     r=kw_args['dividend']%kw_args['divisor']
#     return q,r

# N1=int(input("enter the dividend\n"))
# N2=int(input("enter the divsor\n"))

# T=div_mod(divisor=N2,dividend=N1)
# print("The quotient and remainder are\n",T)

# def display_data(**dl):
#     for k in dl:
#         print(k,dl[k])
# display_data(cringe="i love you")
# display_data(number=10,cringe="i love you")
# display_data(pi_n=3.14287,number=10,cringe="i love you")

#functional programming
# def display_data(p,q,r):
#     print(p**2)
#     print(round(q,2))
#     print(r.title())

# D=display_data
# D(10,3.14287,"god bless you")


#fruitful function

# def sum_cubes(n1,n2,n3):
#     sum3=n1**3+n2**3+n3**3
#     return sum3

# S=sum_cubes
# print("The result is",S(1,2,3))

#passing function as argument
# def display_data(p,q,r,sum_cubes):

#  print(p**2)

#  print(round(q,2))

#  print(r.title())

#  print(sum_cubes(1,2,3))

# display_data(10,3.1428,'god bless',sum_cubes)

# def sum_cubes(*var_arg):
#     sum3=0
#     for j in var_arg:
#         sum3+=j**3
#     return sum3
# S=sum_cubes    
 
# def display_data(p,q,r,s):
#     print(p**2)
#     print(round(q,2))
#     print(r.title())
#     print(s(1,2,3,4))
# D=display_data
# D(10,3.18247,"god bless you",S)    

#lambda function
# are single expression

# def apply(fx,value):
#     return 6+ fx(value)


# double= lambda x:x*2
# cube=lambda x:x*x*x
# avg=lambda x,y,z: (x+y+z)/3

# print(double(5))
# print(cube(5))
# print(avg(3,5,10))
# print(apply(lambda x: x*x*x,2))

#map 
# def cube(x):
#     return x*x*x

# print(cube(2))

# l=[1,2,4,6,4,3]
# newl=[]
# for items in l:
#     newl.append(cube(items))

# print(newl)
# newl= list(map(lambda x:x*x*x,l))
# print(newl)

#FILTER
# def filter_function(a):
#     return a>2
# newnewl=list(filter(filter_function,l))
# print(newnewl)

#REDUCE
# from functools import reduce

# number=[1,2,3,4,5,]
# number=[1,2,3,4,5,]

# sum=reduce(lambda x,y: x+y, number)
#by help of lambda it can be done as
# def mysum(x,y):
#     return(x+y)

# sum=reduce(mysum,number)
  
# print(sum)

#NUMPY
# import numpy as np
# d={'1':'A'}

#multi dimensional array

# a_mul=np.array([[[1,2,3,1],
#                [4,5,6,1],
#                [7,8,9,1]],
#                [[1,1,1,1],
#                 [1,1,1,1],
#                 [1,1,1,1]]])
               
# print(a_mul[0])
# print(a_mul[0,1])

# print(a_mul.shape)
# print(a_mul.ndim)
# print(a_mul.size)
# print(a_mul.dtype)

# a=np.array([[1,2,3],
#             [4,5,6],
#             [7,8,9]])
# print(a.dtype)
# print((a[0][0].dtype))
# print(a[1,1])

# a=np.array([[1,2,3],
#             [4,d,6],
#             [7,8,"hello"]])
# print(a.dtype)
# print(type(a[1][0]))

# import numpy as np

# x=np.array([1,2,3,4])
# print(x)
# print(type(x))
# y=np.arrya([1,2,3,4])
# print(y)
# print(type(y))
# print(y.ndim)

# a=np.array([1,2,3,4])
# print(a)

# x=[1,2,3,4]
# y=np.array(x)
# print(y)

# l=[]

# for i in range(1,5):
#     int_1=int(input("enter the value:"))
#     l.append(int_1)
# print(np.array(l)) 
# print(l.ndim)   

#use ndim to check the dimensin of array

# ar2=np.array([[1,2,3,4],[4,5,6,7]])
# print(ar2)
# print(ar2.ndim)

# ar3=np.array([[[1,2,3,4],[7,8,9,4],[77,88,99,45]]])
# print(ar3)
# print(ar3.ndim)

# arn=np.array([1,2,3,4],ndim=10)
# print(arn)
# print(arn.ndim)

#creating array using numpy function

#0's 
# ar_zero=np.zeros(4)
# ar_zeros=np.zeros((3,4))
# print(ar_zero)
# print()
# print(ar_zeros)

#1's
# ar_one=np.ones(3)
# print(ar_one)
# print(np.one((4,3)))

#empty array
# ar_em=np.empty(4)
# print(ar_em)

#range array
# ar_rn=np.arange(4)
# print(ar_rn)

#array diagonal element filled with 1's
# ar_dia=np.eye(3)
# print(ar_dia)

# arr_dia=np.eye(3,5)
# print(arr_dia)

#linspace=array with an random interval
# ar_lin=np.linspace(0,10,num=5)
# print(ar_lin)

#numpy array creation with random number
#function used are
#rand():generate random value
# var=np.random.rand(4) #1d array of value 4
# print(var)
# var1=np.random.rand(2,5)
# print(var1)

#randn():random value close to zero and number returned maybe +ve or -ve
# var2=np.random.randn(5)
# print(var2)


#ranf():for doing random sampling numpy
# var3=np.random.ranf(3)
# print(var3)

#randint() the function is used to generate random number in a given range
# var4=np.random.randit(min,max,total_values)
# var4=np.random.randint(5,20,5)
# print(var4)

#matplotlib'
# import matplotlib.pyplot as plt
# x=["python","c","c++","java"]
# y=[85,70,60,82]

# plt.bar(x,y)
# plt.show()


# // #include<stdio.h>
# // #include<conio.h>
# // #include<stdlib.h>
# // int i,j,k,a,b,u,v,n,ne=1;
# // int min,mincost=0,cost[9][9],parent[9];
# // int find(int);
# // int uni(int,int);
# // void main()
# // {
	
# // 	printf("\n\tImplementation of Kruskal's algorithm\n");
# // 	printf("\nEnter the no. of vertices:");
# // 	scanf("%d",&n);
# // 	printf("\nEnter the cost adjacency matrix:\n");
# // 	for(i=1;i<=n;i++)
# // 	{
# // 		for(j=1;j<=n;j++)
# // 		{
# // 			scanf("%d",&cost[i][j]);
# // 			if(cost[i][j]==0)
# // 				cost[i][j]=999;
# // 		}
# // 	}
# // 	printf("The edges of Minimum Cost Spanning Tree are\n");
# // 	while(ne < n)
# // 	{
# // 		for(i=1,min=999;i<=n;i++)
# // 		{
# // 			for(j=1;j <= n;j++)
# // 			{
# // 				if(cost[i][j] < min)
# // 				{
# // 					min=cost[i][j];
# // 					a=u=i;
# // 					b=v=j;
# // 				}
# // 			}
# // 		}
# // 		u=find(u);
# // 		v=find(v);
# // 		if(uni(u,v))
# // 		{
# // 			printf("%d edge (%d,%d) =%d\n",ne++,a,b,min);
# // 			mincost +=min;
# // 		}
# // 		cost[a][b]=cost[b][a]=999;
# // 	}
# // 	printf("\n\tMinimum cost = %d\n",mincost);
# // 	getch();
# // }
# // int find(int i)
# // {
# // 	while(parent[i])
# // 	i=parent[i];
# // 	return i;
# // }
# // int uni(int i,int j)
# // {
# // 	if(i!=j)
# // 	{
# // 		parent[j]=i;
# // 		return 1;
# // 	}
# // 	return 0;
# // }