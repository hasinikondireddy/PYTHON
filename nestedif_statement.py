#question 1 
username = input("enter username: ")
password = int(input("enter password: "))
if (username == "admin123"):
    if (password == 1234):
        print("login successful")
        
    else:
        print("wrong password")
else:
    print("wrong username")

#question 2 
a = float(input("enter first number:"))
b = float(input("enter second number: "))
operator = input("enter operator (+, -, *, /): ")
if operator == "+":
    print("result:", a+b)
elif operator == "-":
    print("result:", a-b)
elif operator == "*":
    print("result:", a*b)
elif operator == "/":
    if b!=0:
        print("result:",a/b)
    else:
        print("error: division by zero is not allowed")
else:
    print("invalid operator")

#question 3
marks = int(input("enter marks: "))
attendance = int(input("enter attendance percentage: "))
if marks >= 40:
    if attendance >= 75:
        print("pass")
    else:
        print("fail due to low attendance")
else:
    print("fail due to low marks")

#question 4
balance = float(input("enter account balance: "))
amount = float(input("enter withdrawal amount: "))
if amount > 0:
    if amount <= balance:
        balance =  balance - amount
        print("withdrawal successful")
        print("remaining balance:", balance)
    else:
        print("insufficient balance")
else:
    print("invalid withdrawal amount")

#question 5
age = int(input("enter age: "))
test = input("did you pass the driving test? (yes/no): ")
if age >= 18:
    if test == "yes":
        print("eligible for driving license")
    else:
        print("pass the driving test first")
else:
    print("not eligible due to age")

#question 6 
