a = 6
b = 66
c = 66.666666
d = "asad"
e = True


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#Exercise:1 Basic Varibales and Operation
print("Exercise 1: ==========================")
a = 30
b = "Asad"
c = 30.33
print(f"a = {a}, type: {type(a)}")
print(f"b = {b}, type: {type(b)}")
print(f"c = {c}, type: {type(c)}")

#Exercise:2 Valid and Invalid Variable Names:
print("Exercise 2: ============================")
valid_names = ['name1', '_name', 'name_with_underscore']
invalid_names = ['1name', 'name with space']
print("Valid Variable Names: ")
for name in valid_names:
    print(name)
print("Invalid Variable Names: ")
for name in invalid_names:
    print(name)

#Exercise 3: Arithematic Operations:
print("Exercise 3: ============================")
a = int(input("Please Enter first number: "))
b = int(input("Please Enter second number: "))

print(f"Addition of {a} and {b} is = {a+b}")
print(f"Subtraction of {a} and {b} is = {a-b}")
print(f"Multiplication of {a} and {b} is = {a*b}")
print(f"Division of {a} and {b} is = {int(a/b)}")

#Exercise 4: comparision operators using Logical Operations:
print("Exercise 4: ============================")

a = int(input("Enter your first Number: "))
b = int(input("Enter your second Number: "))
x = True
y = False

if(a>b):
    print(f"{a} > {b}, A is greater then B")
    print(x)
elif(a<b):
    print(f"{a} < {b}, B is greater then A ")
elif(a==b):
    print(f"{a} == {b}, A is equal to B")
else:
    print(y)

#Exercise 5: Taking User Input:
a = input("Please Enter your first Name: ")
b = input("Please Enter your last Name: ")
c = int(input("Please Enter your Age: "))
d = input("Please Enter your Address including post Code: ")
e = int(input("Please Enter your phone number :"))
print("=============OUTPUT===============")
print(f"First Name : {a}, type :{type(a)}")
print(f"Last Name: {b}, type :{type(b)}")
print(f"Age: {c}, type: {type(c)}")
print(f"Address : {d}, type: {type(d)}")
print(f"Phone Number : {e}, type: {type(e)}")
