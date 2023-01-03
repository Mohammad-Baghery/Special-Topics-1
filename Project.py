
import math
num=int(input("Enter a Number Between 1 to 9: "))
match num:
    case 1:
        print("Perimeter and Area for Circle: ")
        r = float(input("Enter the Radius: "))
        print("Area:         ",(r*r)*math.pi)
        print("Perimeter:  ",(r*2)*math.pi)
    case 2:
        print("Perimeter and Area for Square: ")
        s = float(input("Enter the Side: "))
        print("Area:         ",s*s)
        print("Perimeter:  ",s*4)
    case 3:
        print("Perimeter and Area for Triangle: ")
        b1 = float(input("Enter Base 1: "))
        b2 = float(input("Enter Base 2: "))
        b3 = float(input("Enter Base 3: "))
        if b1>b2 and b1>b3:
            b=b1
        elif b2>b1 and b2>b3:
            b=b2
        elif b3>b1 and b3>b2:
            b=b3
        else:
            b=b2
        h = float(input("Enter Height: "))
        print("Area:        ",(b*h)/2)
        print("Perimeter: ",b1+b2+b3)
    case 4:
        print("Perimeter and Area for Trapezius: ")
        sb = float(input("Enter the Small Base: "))
        bb = float(input("Enter the Big Base:    "))
        ss = float(input("Enter the Small Side:    "))
        bs = float(input("Enter the Big Side:    "))
        h = float(input("Enter the Height:         "))
        print("Area:        ",((sb+bb)/2)*h)
        print("Perimeter: ",(sb+bb)+(ss+bs))

    case 5:
        print("Perimeter and Area for Polygon: ")
        ns = float(input("Enter number of Sides: ")
        ls = float(input("Enter Length of One Side: ")
        
