#read file
# f=open('filehandling.txt','r')
# print(f'cursor position-{f.tell()}')
# print(f.read())
# print(f.readline(),end='') #read one at a time
# print(f'cursor position-{f.tell()}')
# print('before seek method')
# f.seek(0)
# print('after seek method')
# print(f'cursor position-{f.tell()}')
# print(f.read())
# print(f.read)

# lines=f.readlines()
# print(lines)
# print(len(lines))
# for line in lines:
#     print(lines,end='')

#data encscripter tells the name of file
#two data enscriter
# print(f.name)
# print(f.closed)
# for line in f.readlines()[:2]:
#     print(lines,end='')
# f.close()    
# f.close()
# print(f.closed)

#With blocks: contacts manager

# with open('filehandling.txt') as f:
#     data=f.read()
#     print(data)

# print(f.closed)    

#READ
# with open('filehandling.txt','r')as f:
#     data=f.read()
#     print(data)

#WRITE

# with open('filehandling.txt','w') as f:
#     f.write('hello there\n subscribe to my channel')

#READ
# with open('filehandling.txt','w') as f:
#     f.write('hello there\n subscribe to my channel')

#append
# with open('filehandling.txt','a') as f;
# f.write('hi welcome to my channel')

ith open('filehandling2.txt','a') as f;
f.write('hi welcome to my channel')