#type conversion
x=5.6       #int
y=7     #float
z="hello"   #str
y=x*y
print("type of y is ",type(y))
print(type(x))
print(type(y))
print(type(z))
# explicit type of conversions
age=input("what is your ages?\n")
age=int(age)
print(age,type(float(age))) 
name=input("what is your name? \n")
print(name,type(int(name)))