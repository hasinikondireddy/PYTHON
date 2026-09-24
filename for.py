#use for loop when you know how many times you want to repeat
#print number from 1 to 10 
for i in range(1, 11):
    print(i)

for i in range(10,0,-1):
     print(i)

#even numbers from 1 to 50
for i in range(0,51,2):
    print(i)

#odd numbers from 1 to 50
for i in range(1,51,2):
    print(i)

#print even numbers from 2 to 50
for i in range(2,51,2):
    print(i)

#print multiples of 5 from 5 to 50
    for i in range(5,51,5):
        print(i)

#multiplication table 
num = int(input("enter number: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#sum of numbers from 1 to n
n = int(input("enter number: "))
total = 0   
for i in range(1,n+1,1):
    total = total + i
print("sum=",total)

#factorial of numbers
n = int(input("enter number: "))
factorial = 1
for i in range(1,n+1,1):
    factorial = factorial * i
print("factorial =",factorial)

#sum of even numbers from 2 to n
n = int(input("enter number: "))
total = 0
for i in range(2,n+1,2):
    total = total + i
print("sum=",total)

#count of multiples of 3
n = int(input("enter number: "))
count = 0
for i in range(1,n+1,1):
    if i%3 == 0:
        count = count + 1
print("count: ",count)

#sum of multiples of 5
n= int(input("enter number  n: "))
total = 0
for i in range(1,n+1):
    if i%5 == 0:
        total = total + i
print("sum = ",total)

#check if a number is prime
number = int(input("enter a number"))
count = 0
for i in range(1, number+1):
 if number%i == 0:
  count = count + 1
  if count == 2:
     print("prime number")
  else:
     print("not a prime number")

#print all prime numbers between 2 and 100
for number in range(2,101):
    count = 0
    for i in range(1, number + 1):
        if number%i == 0:
            count = count + 1

    if count == 2:
        print(number)

#find the first number between 1 and 100 that is divisible 
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("first number:",i)
        break

#password check with limited attempts
    total = 0
    for i in range(10):
        number = int(input("enter number:"))
    if number > 0:
        continue
    total = total + number

    correct_password = "python123"
    for attempt in range(1,4):
        password = input("enter password: ")
        if password == correct_password:
            print("login successful")
            break
        print("wrong password")
else:
    print("account locked")

#find the largest among 5 numbers  entered by the user
largest = None
for i in range(5):
    number = int(input("enter number: "))
    if largest is None or number > largest:
        largest = number
        print("largest:",largest)

    #find the smallest number among 5 number entered by the user
    smallest = None 
    for i in range(5):
        number = int(input("enter number: "))
        if smallest is None or number < smallest:
            smallest = number
print("smallest:",smallest)