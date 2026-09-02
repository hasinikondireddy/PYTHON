#operators
a = 15
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

#simple calculator
a = int(input("enter first number:"))
b = int(input("enter second number:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#student marks calculator
a = int(input("enter english marks"))
b = int(input("enter maths marks"))
c = int(input("enter social marks"))
total = a+b+c
avg = total/3
print(total)
print(avg)

#shopping bill calculator
p1 = float(input("enter product1 price"))
p2 = float(input("enter product2 price"))
p3 = float(input("enter product3 price"))
total = p1+p2+p3
discount = total*0.10
final_amount = total - discount 
print(final_amount)

#salary calculator
basic = float(input("enter basic salary:"))
hra = basic*0.20
da = basic*0.10
gross_salary = basic+hra+da
print("basic salary;",basic)
print("HRA:",hra)
print("DA:",da)
print("gross salary:",gross_salary)
