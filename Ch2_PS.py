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