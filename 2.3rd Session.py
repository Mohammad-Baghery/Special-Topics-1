#3rd Session
num1=int(10)
num2=int(5)
print("{}=={1}:{2}".format(num1,num2,num1==num2))
print("{}!={1}:{2}".format(num1,num2,num1==num2))
print("{}<>{1}:{2}".format(num1,num2,num1==num2))
print("{}<{1}:{2}".format(num1,num2,num1==num2))

# & examples
Resault=(5&3)
print(Resault)
resault=(5/3)
print(resault)

#xor Example
print(5^3)

#Shifting Examples
x=10<<2
print(x)
y=10>>2
print(y)

#Membership Examples
print(5 in [8, 3, 5, 20])
print(5 not in [8, 3, 5, 20])

#Identity Examples
number1=5
number2=6
print(number1 is number2)
print(number1 is not number2)

#input Examples
name=input("Enter Your Name: ")
age=input("Enter Your Age: ")

#if & else Examples
A=15
B=16
if(A>B):
    print("A>B")
else:
    print("A<B")

#HomeWork: receive 2 nums and calculate are they divisible to eachother or not
Num1=int(input("Enter Number 1: "))
Num2=int(input("Enter Number 2: "))
if Num1/Num2==0:
    print("Divisible")
else:
    print("Undivisible")

#HomeWork 2: receive 3 nums and calculate can the build a tiangle
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
num3=int(input("Enter Third Number: "))
if((num1+num2>num3) and (num1+num3>num2) and (num3+num2>num1)):
    print("Perimeter Is: ",(num1+num2+num3))
else:
    print("They Can't make a triangle")
