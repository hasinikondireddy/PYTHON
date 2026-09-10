#comparison operators 
a = 20 
b = 30 

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#age eligibility checker
age = int(input("enter your age"))
print("eligibility:",age >=18)

#pass or fail checker
marks = int(input("enter your marks:"))
print("passed:", marks >= 40)

#login validation 
correct_username = "admin"
correct_password = "1234"

username = input("enter username:")
password = input("enter password:")

print(username == correct_username)
print(password == correct_password)


