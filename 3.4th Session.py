#Write a program who count 0-100 and 100-0
for i in range(101):
    print(i)
for i in range(100, -1 , -1):
    print(i)

#Lists Example:
txt={'Ali','Mohammad','Hossein'}
for text in txt:
    print(text)

#Enumerate Lists
for index,text in enumerate(txt):
    print(index, text)

#program who receive a string and print as charachter:
TXT=input("Enter a String: ")
for i in TXT:
    print(i)

#Example for range
for i in range(5):
    print(i)

#Write a program who receive 2 Numbers from user and count numbers between them ascending:
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
if num2>num1:
    temp=num1
    num1=num2
    num2=temp
for i in range(num2,num1):
    print(i)

#program who draw Triangle with *:
#First Way:
for i in range(1,5):
    print('*'* i)
#Second Way:
for i in range(1,5):
    for j in range(i):
        print('*', end="    ")
    print()

#Draw a Multiplication Table:
for i in range(1,10):
    for j in range(1,10):
        print(i*j,end= "\t")
    print("\n")

#Program who sum the Even Numbers between 1 and 100
Sum=0
for i in range(0,101,2):
        Sum+=i
print(Sum)

#Program who receive a number and calculate Factorial:
b=1
a=int(input("Enter a Number: "))
a+=1
for i in range(1,a,1):
    b=b*i
print(b)

