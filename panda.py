#pandas

#series
# import pandas as pd
# x=[3,4,5,6]
# var=pd.Series(x)
# print(var)
# print(type(var))
# print(var[2])

# x=[3,4,5,6]
# var=pd.Series(x,index=['a','s','d','f'],dtype=float,name="python")
# print(var[2])
# print(var)

# dic={"name":['python','c++','c','java'],"por":[12,13,14,15],"rank":[1,4,3,2]}

# var1=pd.Series(dic)
# print(var1)

# s=pd.Series(12,index=[1,2,3,4,5,6])
# print(s)
# print(type(s))

# s1=pd.Series(12,index=[1,2,3,4,5,6,7])
# s2=pd.Series(12,index=[1,2,3,4])

# print(s1+s2)

#DATA FRAME IN PANDA

# import pandas as pd

# l=[1,2,3,4]
# var=pd.DataFrame(l)
# print(var)
# print(type(var))

# d={"a":[1,2,3,55,5],"s":[1,2,3,4,5],"d":[1,2,3,4,5],1:[1,2,3,4,5]}
# var1=pd.DataFrame(d)
# print(type(var1))
# print(var1)
# print(var1["a"][3])

# list_1=[[1,2,3,4,5],[11,12,13,14,15]]

# var2=pd.DataFrame(list_1)

# print(type(var2))
# print(var2)

# sr={"s":pd.Series([1,2,3,4]),"r":pd.Series([1,2,3,4])}

# var3=pd.DataFrame(sr)

# print(type(var3))
# print(var3)

#ARITHEMATIC OPERATIONS
# var=pd.DataFrame({"A":[10,20,30,40],"B":[15,16,17,18]})
# var["C"]=var["A"]+var["B"]
# var["C"]=var["A"]-var["B"]
# var["C"]=var["A"]*var["B"]
# var["C"]=var["A"]/var["B"]
# print(var)

# var["python"]=var["A"]<=20
# var["python_1"]=var["B"]>=16

# print(var)

#insertion 

# var=pd.DataFrame({"A":[1,2,3,4,5],"B":[9,8,7,6,5]})
# print(var)
# var.insert(1,"python",var["A"])
# print(var)

# print(var.insert(1,"python_1",[11,12,13,14,15]))


# var=pd.DataFrame({"A":[1,2,3,4,5],"B":[9,8,7,6,5]})
# print(var)
# var["python_12"]=var["A"][:3]
# print(var)

#DELETE

# var=pd.DataFrame({"A":[1,2,3,4,5],"B":[9,8,7,6,5],"C":[11,12,13,14,15]})
# var1=var.pop("B")
# print(var1)
# print(var)
# del var["A"]
# print(var)
