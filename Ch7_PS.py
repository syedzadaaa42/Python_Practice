# #This Chpater is about loops in python using define functions 

# #Exercise 1: Write a program to find the multiple table of the user input 

# def multiplication_table(user):
#     for i in range(1, 11):
#         print(f"{user}x{i}={user*i}")

# multiplication_table(int(input("please Enter a Number: ")))

# #Exercise 2: Greet names starting with S in the list:
# def greet_names(names):
#     for name in names_list:
#         if name.startswith('A'):
#             print(f"Hello {name}")

# names_list = ["Somia", "Subhan", "Airshad", "Rakir", "Asad"]
# greet_names(names_list)

# #Exercise 3: Multiplication table using while loop:

# def multiplication_table(n):
#     i = 0
#     while i<11:
#         print(f"{n} x {i} = {n*i}")
#         i=+1
# multiplication_table(n=int(input("Please Enter a Number: ")))

#Exercise Star patterns: 
#Simple traingle:
print("Simple Triangle:")
n = 5
for i in range(1, n+1):
    print("* "*i)

#Inverted Triangle Pattern:
print("Inverted Triangle Pattern")
n = 5
for i in range(n, 0, -1):
    print("* "*i)

#right Angle Triangle Pattern:
print("Right Angle Triangle Pattern:")
n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "*"*i)

#Pyramid Pattern:
print("Pyramid Pattern: ")
n =5
for i in range(1, n+1):
    print(" "*(n-i)+"*"*(2*i-1))

#Inverted Pyramid Pattern:
print("Inevrted Pyramid")
n = 5 
for i in range(n, 0, -1):
    print(" "*(n-i)+"*"*(2*i-1))

#Multiplication program in reverse:
table = int(input("Please Enter a number: "))
for i in range(10, 0, -1):
    print(f"{table} x {i} = {table*i}")
    