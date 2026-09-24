#question 1 
a = 10 
b = 20
if a>=15:
    print("a is greater than b")
elif a>=20:
    print("a is equal to b")
else:
    print("a is less than b")

#question 2
#we can use elif statement as many times as we want
#using 'and' operator
marks = int(input("enter marks: "))
if marks>=90:
    print("grade A")
elif marks<=89 and marks>=60:
    print("grade B")
elif marks<=59 and marks<=35:
    print("grade C") 
else:
    print("grade D")

#question 3 
marks = int(input("enter marks"))
if marks>=90:
    print("grade A")
elif marks >=75:
    print("grade B")
elif marks>=60:
   print("grade C")
elif marks>=40:
    print("grade D")
else:
    print("fail")

#question 4 
#greatest of three numbers
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
c = int(input("enter 3rd number: "))
if a>b and a>c:
    print("a is the greatest")
elif b>a and b>c:
    print("b is the greatest")
else:
    print("c is the greatest")

#question 5
#largest of two numbers 
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
if a>b:
    print("a is largest")
elif b>a:
    print("b is largest")
else:
    print("both are equal")

#question 6
num = int(input("enter a number: "))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

#question 7
day = int(input("enter day number: "))
if day == 1:
    print("monday")
elif day == 2:
    print("tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("friday")
elif day == 6:
    print("saturday")
elif day==7:
    print("sunday")
else:
    print("invalid day")

#
