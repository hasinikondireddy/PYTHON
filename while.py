#print all even numbers from 2 to 50
i= 2
while i<=50:
    print(i)
    i = i + 2

 #print all odd numbers from 1 to 50
i= 1    
while i<=50:
    print(i)
    i = i + 2

 #print total of number entered by user until 0 is entered 
total = 0
n = int(input("enter number: "))
while n != 0:
    total = total + n
    n = int(input("enter number: "))
    print("Total:", total)

#password check 
password = ""
while password != "python123":
    password = input("enter password: ")
print("login successful")

#count the number of digits in a number 
number = int(input("enter number: "))
count = 0
while number > 0:
    number = number//10
    count = count + 1
print("number of digits:" ,count)

#sum of digits 
number = int(input("enter number: "))
total = 0
while number > 0:
    digits = number%10
    number = number//10
    total = total + digits
print("sum of digits: ",total)

#reverse a number
number = int(input("enter number: "))
reverse = 0
while number > 0:
    digit = number%10
    number = number//10
    reverse = reverse*10 + digit
    print("reverse: ",reverse)

#check if a number is a palindrome
number = int(input("enter number: "))
original = number
reverse = 0
while number>0:
    digit = number%10
    reverse = reverse*10 + digit
    number = number//10

    if original == reverse:
     print("palindrome")
    else:
        print("not palindrome")

#calculate the sum of positive numbers entered by the user
total = 0
while True:
    number = int(input("enter number: "))
    if number > 0:
        continue
    if number == 0:
        break
    total = total + number
    print("total: ",total)




