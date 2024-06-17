#This Chapter is about List and Tuples:
#Creating and indexing List:
friends = ["Asad", "Noor", "Ali Raza", "Zohaib", 9, False]
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print(friends[5])

#List Slicing:
print(friends[0:3])

#List Methods: sort, Reverse, Append, insert, Remove methods:
l1 = [1, 8, 9, 4, 5, 10]
#Sort Method: Sorts the list in Accending order
l1.sort()
print(l1)
#Reverse Method: Sorts the list in Decending order
l1.reverse()
print(l1)
#Append Method: Adds a number to the end of the list 
l1.append(1000)
print(l1)
#insert Method: Adds a number to a specified place (Place, argument)
l1.insert(0, 55)
print(l1)
#Remove Method: Removes the number or tyhe argument form the list:
l1.remove(5)
print(l1)

#>>>>>>>>>>>>>>>TUPLE<<<<<<<<<<<<<<<<<<<#


a = (1, 2, 3, 4, 5, 1)
#Find the number of accurances of an argument:
print(a.count(1))
#Find the index number of the first accurance of the argument:
print(a.index(4))
