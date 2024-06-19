#This Chapter is about IF and Else Statement:

#Exercise 1:Find the Greatest of four Number Entered by the user
numbers = []
for i in range(4):
    number = int(input(f"Please Enter number{i+1}: "))
    numbers.append(number)

greatest = max(numbers) # max method is used to find the greatest number
print("The greatest number is: ", greatest)

#Exercise 2: Determine if the stduent passes or fails:
subjects = ["English", "Maths", "Physics"]
marks = []

for subject in subjects:
    mark = int(input(f"Please Enter the marks for {subject}: "))
    marks.append(mark)

total_marks = sum(marks)
total_percentage = (total_marks/300)*100
subject_pass = all(mark >=33 for mark in marks)
if (total_percentage>=40 and subject_pass):
    print("The Student has Passed !")
    print(f"The Percentage is :{total_percentage} ")
    print(f"The total marks: {total_marks}")
else: 
    print("The student has failed !")

#Exercise 3: Detect Spam Comments:
spam_comment = ["Subscribe to this", "Signup Now", "Buy now"]
comment = input("Enter a Comment : ")

is_spam = any(keyword in comment for keyword in spam_comment)
if is_spam:
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")
    
#Exercise 4: Check if the username contains less than 10 characters:
username = input("Enter a username: ")
if len(username)<10:
    print("the Length of the username contains less than 10 characters")
else:
    print("The length of the username contains more than 10 character")

Exercise 4: Check if the post mentions harry:
post = input("Please Enter a post: ")
if "harry" in post:
    print("The post is talking about Harry !")
else: 
    print("The post is not talking about harry !")