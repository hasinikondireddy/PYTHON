
for i in range(1,11):
    print(i)
    if i == 7:
        break

i = int(input())
while i <=50:
    print(i)
    i = i + 1
    if i == 5:
        break

for i in range(1,11):
    if i == 7:
        print('number found')
        break
    print(i)

#print numbers until user enters 0
while True:
    number = int(input("enter number: "))
    if number == 0:
        break
    print("you entered:",number)

#print numbers from 1 to 100, but skip multiples of 3 and stop at 50
for i in range(1,101):
    if i == 50:
        break
    if i%3 == 30:
        continue
    print(i)