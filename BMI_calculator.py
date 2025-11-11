# its a BMI calculator python program

height = input(" enter your height")
weight = input(" enter your weight")

bmi = int(weight) / float(height) ** 2 

print(type(height)) 
print("your BMI is ",bmi)
bmi_as_int= int(bmi)
print(bmi_as_int)
'''
we may convert the float point bmi into the whole by type casting it to an integer
using the type cast
'''