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

