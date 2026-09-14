#question 1
total_mins = int(input("enter no.of mins:"))
hours = total_mins//60
remaining_mins = total_mins % 60
total_sec = total_mins * 60
print(hours)
print(remaining_mins)
print(total_sec)

#question 2 
#display personal details using variables
name = str(input("enter name:"))
age = int(input("enter age:"))
height = float(input("enter height:"))
print(name)
print(age)
print(height)

#question 3
#personalized greeting
name = input("enter name:")
print(f"hello,{name}!")

#question 4 
#power calculation
base = int(input("enter base:"))
exponent = int(input("enter exponent:"))
print(base**exponent)

#question 5
#average of three numbers
a = int(input("enter 1st number"))
b = int(input("enter 2nd number:"))
c = int(input("enter 3rd number"))
total = a+b+c
avg = total/3
print(avg)

#question 6 
#greater than comparision
a = int(input("enter 1st number:"))
b = int(input("enter 2nd number:"))
print(a>b)

#question 7
#equality check
a = int(input("enter 1st number"))
b = int(input("enter 2nd number"))
print(a==b)

#question 8
#add two numbers read as strings
a = input()
b = input()
#converting the string into integer
a = int(a)
b = int(b)
total = a+b
print(total)

#question 9
#float to integer conversion
n = float(input())
print(n)
new = int(n)
print(new)

#question 10
#sum using arthematic operator
a = int(input())
b = int(input())
print(a+b)

#question 11
#area of a rectangle
length = float(input())
breadth = float(input())
area = length*breadth
print(area)

#question 12
#quotient and remainder 
a = int(input())
b = int(input())
q = a/b
r = a%b
print(q)
print(r)

#question 13
#both numbers positive check
n1 = int(input())
n2 = int(input())
print(n1>0 and n2>0)

#question 14
#atleast one even number 
#even number: if the number is divisible by 2 without any remainder
n1 = int(input())
n2 = int(input())
print(n1%2==0 or n2%2==0)

#question 15
#logical NOT on a condition
#logical NOT - reverse result
num = int(input())
print(not(num>0))

#question 16
#augmented assignment operations
a = int(input())
a = a+5
a = a*2
a = a-3
print(a)

#question 17
#exchange values of two variables 
a = int(input())
b = int(input())

# Logic 1 - Using temp variable
temp = a
a = b
b = temp
print(a)
print(b)

# Logic 2: Without using temp (3rd variable)
a=a+b
b=a-b
a=a-b
print(a)
print(b)

# Logic 3: Without using temp (3rd variable)
a = a^b
b = a^b
a = a^b
print(a)
print(b)

# Logic 4: Without using temp (3rd variable)
# Problem: It cannot handle 0
a = a*b
b = a/b
a = a/b
print(a)
print(b)

# Logic 5: Using Python's Special
# Simplest Way
a,b = b,a
print(a)
print(b)

#question 18
#calculate simple intrest 
principle = float(input())
rate = float(input())
time = float(input())
si = (principle*rate*time)/100
print(si)

#question 19
#temperature conversion(celsius to fahrenheit)
c = float(input())
f = (c*9/5)+32
print(f)

#question 20
#check divisibility by 3 and 5 
n = int(input())
print(n%3==0 and n%5==0)

#question 21 
#sum of digits of a two digit number
num = int(input())
tens = num//10
units = num%10
total = tens + units
print(total)

