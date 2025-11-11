# strings are immutable
a="abhishek"
print(len(a))
print(a.upper())
b="ABHISHEK"
print(b.lower()) 
c="Abhishek!!!"
print(c.rstrip("!"))
d="!Abhi"
print(d.rstrip("!"))
e="!!!Anish"
print(e.replace("Anish","gabbar"))
f="Rajiv and megha"
print(f.split(" "))
g="aBHI"
print(g.capitalize())
blogHeading="intro to js"
print(blogHeading.capitalize())
str1="Welcome to console!!!"
print(len(str1))
print(len(str1.center(50)))
h="ram ram bhai"
print(h.count("ram"))
i="see ya soon"
print(i.endswith("soon"))
j="talk to you later"
print(j.endswith("hi"))
k="Welcome to the console !!!"
print(k.endswith("to",4,10))

Str2="He's name is dan. He is an honest mam."
print(Str2.find("is"))
str3="he is abhi. He is an honest man"
print(str3.find("an"))

str4="welcometotheconsole"
print(str4.isalnum())

str5="hello world"
print(str5.islower())
str6="we wish you a happy diwali"
print(str6.isprintable())

str7="    " #using spacebar
print(str7.isspace())

x="Let Me Love You"
print(x.istitle())

v="Hi i am a good boy"
print(v.title()) 

