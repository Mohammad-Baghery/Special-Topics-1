#Program to model 100 arrays (smoothing pictures)
LST=[]
LST2=[]
for i in range(100):
    j=input("Enter 100 Numbers: ")
    LST.append(j)
LST2.append(LST[0])
for i in range(1,len(LST)-1):
    j=LST[i-1]+LST[i]+LST[i+1]
    j=j/3
LST2.append(LST[99])
print(LST2)

#Shift to left and right:
def shift():
    a=[]
    c=[]
    for i in range(10):
        j=input("Enter 10 Numbers: ")
        a.append(j)
    b=input("Enter 1 or 2: ")
    if b==1:
        c=a<<3
    elif b==2:
        c=a>>3
    print(c)
shift()

#Biggest and smallest number in array:
def lower_upper(array):
    array.sort()
    print(array[0])
    print([99])

#Search in 2D array:
B=-1
A=input("Enter the Number: ")
for i in arr:
    for j in i:
        if A==j:
            B=A
    if B==-1:
        print("NOT Found")
    else:
        print(B)

#A program who fills a 5*5 with 0:
arr=[]
cols,rows=5,5
for i in range(rows):
    cols=[]
    for j in range(cols):
        cols.append(0)
    arr.append(cols)
print(arr)
