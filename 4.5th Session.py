#5th Session Homeworks
#input 2 numbers and count (EX1)
#B1=Max Number & B2=Min Number
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
STR=input("Enter a charachter between D or U : ")
if(num1>num2):
    B1=num1
    B2=num2
else:
    B1=num2
    B2=num1
if(STR=='u' or STR =='U'):
    for i in range(B1,B2+1):
        print(i)
elif(STR=='d' or STR =='D'):
    for i in range(B2,B1+1):
        print(i)
else:
    print("Input Charachter NOT Correct!")

#Index Examples in list:
Name=["ABC","DEF","GHI"]
x=Name[0]
print(x)

#Len Example:
Y=len(Name)
print(Y)

#For exapmle in Lists:
for i in Name:
    print(i)

#Add & Remove From Lists:
Name.append("JKL")
Name.pop(0)
print(Name)

#input 5 names and print them
name=[]
for i in range(0,5):
    STR=input("Enter Names: ")
    name.append(STR)
for i in name:
    print(i)

#input 100 Numbers and find the Max:
temp=0
num=[]
for i in range(0,101):
    STR=input("Enter Numbers: ")
    num.append(int(STR))
for i in num:
    if(i>temp):
           temp=i
print(temp)

#Find the Max Repeats in last example:
c=0
temp=0
num=[]
for i in range(0,101):
    STR=input("Enter Numbers: ")
    num.append(int(STR))
for i in num:
    if(i>temp):
           temp=i
for i in num:
    if(i==temp):
        c+=1
print("Max is : ",temp," And Number of Repeats: ",c)

#make list with 100 random numbers & sort them ascending:
import random
from random import randint
from random import seed
temp=0
Num=[]
for i in range(0,100):
    Num.append(random.randint(0,100))
for i in Num:
    for j in Num:
        if(i>j):
            temp=i
            i=j
            j=temp
print(Num)

#Use Def and plus two imputs:
def Calc(X,Y):
    Z=X+Y
    print(Z)
A=int(input("Enter First Number: "))
B=int(input("Enter Second Number: "))
Calc(A,B)

#Use Def and plus two imputs and send answer to main def:
def calc(x,y):
    z=x+y
    return z
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=calc(a,b)
print(c)

#Write a KMM program:
def BMM(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            bmm = i 
    return bmm

num1 = int(input("Enter First Number: ")) 
num2 = int(input("Enter Second Number: ")) 
BM=BMM(num1, num2)
print("BMM=", BMM(num1, num2))
print("KMM=",(num1*num2)/BM)

#program to calculate distance between two points
import math
def distance(x1 , y1 , x2 , y2):
    return math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) * 1.0)
h=int(input("Enter X1: "))
i=int(input("Enter X2: "))
j=int(input("Enter Y1: "))
k=int(input("Enter Y2: "))
print("%.6f"%distance(h, i ,j, k))
