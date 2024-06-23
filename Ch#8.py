#This chapter is about Functions and Recursions:
#Simple table function(Exercise 5):
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

table(int(input("Please Enter a number : ")))

#Greeting Function:
def greet(name):
    gr = "Hello "+name
    return gr

a = greet(input("Please Enter your name : "))
print(a)

#Exercise 1: write a fucntion to find greatest of three numbers:
def greatest(a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    
num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the Second Number: "))
num3 = int(input("Enter the third Number: "))
print("The greatest Number is : ", greatest(num1,num2,num3))

#Exercise 2:Celsius to Forenheight:
def cel_to_for(celcius):
    return (celcius * 9/5)+32
    
a= float(input("Please Enter Celcius: "))
forenheight = cel_to_for(a)
print(forenheight)

#Exercise 3: Function to print a pattern:
def pattern(n):
    for i in range(n, 0, -1):
        print("* "*i)
n = int(input("Please Enter the number of lines: "))
pattern(n)

#Exercise 4: Convert inches to centimeters:
def inch_to_cen(inches):
    return inches*2.54

inches = float(input("Please Enter length in inches: "))
cm = inch_to_cen(inches)
print(cm)

