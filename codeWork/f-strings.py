 #f string is used for string formating
letter="hey my name is {} and i am from {}"

country="india"
name="harry"

print(letter.format(name,country))
print(f"hey my name is{name} and i am from {country}")
# if we want to display above text as it is then:
print(f" we use f-string like this: Hey my name is {{name}} andi am from {{country}}")

# txt="for only {price:.2f} dollars"
# print(txt.format(price=50.2155))
price=45.6556
txt=f"for only {price:.2f} dollars"
print(txt)
print(f"{2+30}") #we want to create value inside we can do that too
