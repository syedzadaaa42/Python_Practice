#This Chapter is about Dictionaries and Tuples:

#Exercise 1: Program to create dictionary of hindi and engish translations
Dictionary   = {
    "Kese ho ? ":"How are you ?",
    "Kutta":"Dog",
    "Lund":"Dick",
    "Subah":"Morning",
    "Laal":"Red" ,
    "Chutia":"Idiot"}

word = input("Please Enter the word for english translation: ")

translation = Dictionary.get(word, "word not found")
print(f"The translation of the {word} is : ", translation)

#Exercise 2: Enter eight numbers and display them unique:
numbers = []
for i in range(8):
    number=int(input(f"Please Enter number {i+1}: "))
    numbers.append(number)

unique_number= set(numbers) # set method allows ordered collection of unique elements
print("The Unique Numbers are : ", unique_number)

#Exercise 3: Check to see if the set can have 18 or "18" as values:
s = {18, "18"}
print(s)

#Exercise 4: Length of the set after Operation:

s= set()
s.add(10)
s.add(20)
s.add("20")
print(len(s))

#Exercise 5: Create a Dictionary of favourite language for 4 friends:
fav_lang = {}
for i in range(4):
    name = input("Please Enter your name: ")
    lang= input("Please Enter your favorite Language: ")
    fav_lang[name]= lang

print(f"Favorite language of the following names : {fav_lang}")

