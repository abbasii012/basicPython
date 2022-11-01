
# defining function
# 1
def  print_name():
    print("hello haseeb i am")
    print("here")
    print("i am jandala")

print_name()
# 2
def  print_name():
    text="hello i am haseeb "
    print(text)

print_name() 
#  3
def print_name(text):
     print(text)
 
print_name("haseeb")

# defining a function with if else and elif statement:
def school_calculator(age):
    if age==5:
        print("you can join school")
    elif age>5:
        print("you should join higher school")
    else:
        print("you are still baby")

school_calculator(6)
def future_age(age):
    future=age+20
    return future
    # print(future)
agesforfuture=future_age(3)
print(agesforfuture)