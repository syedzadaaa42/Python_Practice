#Chapter 3: this is about strings and slicing:

#Exercise one: cretain strings:
a = "Asad"
b = 'Asad'
c = """Asad"""
print(a)
print(b)
print(c)

#Exercise 2: String Slicing:
print("String Slicing======================")
name = "AsAd" ## 
print(name[0:3])
print(name[0:4])
print(name[2:4])

#Exercise 3: Slicing with Skip Values:
print(name[1::4])

#Exercise 4: Advance slicing technique:
print(name[-1])
print(name[:-1])

#Exercise 5: Length of string:
print(len(name))

#Exercise 6: Endswith Function:
print(name.endswith("ad")) # True 

#Exercise 7: Count Function:
print(name.count("A"))

#Exercise 8: Capatilize Function:
print(name.capitalize())

#Exercise 9: Find function:
print(name.find("A"))

#Exercise 10: Using Escape Sequence Characters:
print("Hello\nWorld") #Newline
print("Hello\tworld") #Tab
print("It's Python") #Single Quote
print("Bakclash: \\") #Backlash