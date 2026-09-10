#datatypes
a = 10 
print(type(a))
b = 3.14
print(type(b))
phone = True 
print(phone)
print(type(phone))
z = 3+4j
print(z)
print(type(z)) 
name = "pranavi"
print(name)
print(type(name))

#list in python 
#list is an ordered and changeble collection that can strore multiple values.
marks = [80,70,75,60]
print(marks)

#acsessing elements in list
marks = [90,80,65,70]
print(marks[0])
print(marks[1])
print(marks[2])

#change elements in a list 
marks = [90,80,75]
marks[1]= 95
print(marks)

#add elements to a list 
#adds new elements at the end of the list
marks = [90,80,68,75]
marks.append(85)
print(marks)

#remove elements from list 
marks =[90,72,70,80]
marks.remove(90)
print(marks)

#insert elements into list 
numbers = [10,50,40]
numbers.insert(1,20)
print(numbers)

#extend a list 
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

#remove all elements 
numbers = [10,20,30]
numbers.clear()
print(numbers)

#index method
numbers = [10,20,30,40]
print(numbers.index(30)) 

#count method
numbers = [10,20,30,40,50]
print(numbers.count(40))

#sort method
numbers = [10,20,30,40,50]
numbers.sort()
print(numbers)

#reverse sort method 
numbers = [10,40,60,70,20]
numbers.sort(reverse = True)
print(numbers)

#reverse method
numbers = [10,20,30,40,50]
numbers.reverse()
print(numbers)

#copy method
a = [1,2,3]
b = a.copy()
print(b)

numbers = [10,20,30,40,50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

#tuples in python
#tuple is a collectiom of multiple values that is ordered and unchangable.
student = ("Hasini",18,"python")
print(student[0])

#access values in python 
student = ("hasini",18,"python",90.27)
print(student[0])
print(student[1])
print(student[2])
print(student[3])

#immutable nature or tuple
student = ("hasini",18,"python")
student[1]=22
#this gives an error because tuple is not changable 

#tuples are immutable
numbers = (10,20,30,40,50)
print(numbers.count(20))

numbers = (10,20,30,40,50)
print(numbers.index)

numbers = (10,20,30,40,50)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python
#set is a collection of unique values that is unordered and mutable(changable)
numbers = {10,20,30,40,50}
print(numbers)

#why use set?
#suppose students have selected subjects
subjects = {"python","java","SQL","java"}
print(subjects)

#add values top a set 
subjects = {"python","SQL"}
subjects.add("java")
print(subjects)

#remove values from a set 
subjects = {"java","python","SQL"}
subjects.remove("SQL")
print(subjects)

#set do not allow duplicate values
numbers = {1,2,3,4,5,3,2,1}
print(numbers)