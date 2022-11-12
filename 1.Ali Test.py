#HomeWork 2nd Session
#HomeWork Ali Test
_name='Ali'
_family='Test'
_age='28'
print(_name+ '\b' +_family)
print(_age + "2")

#Upper Cases
c='Family'
c=c.upper()
print(c)

#Forming with %
name='test'
price=1.23456
_text='Hello %s name and price is %4.4f and it is good' %(name, price)
print(_text)

#Formating strings with format
print('Message {0:s} text is test {1:f}' .format('one', 3.14))


#Type Casting
A=3.14
B=int(A)
print(B)
C=float(B)
print(C)

#List examples
_userages=[24,20,25,28,30]
print("UserAges = ",_userages)
print("index 1 = ",_userages[1])
print("index -1 = ",_userages[-1])
_userages2=_userages
print("UserAges 2 = ",_userages2)

#Adding part of a list
_userages3=_userages[2:4]
print("UserAges 3 = ",_userages3)

#Slice example
_userages4=_userages[1:5:2]
print("UserAges 4 = ",_userages4)

#Adding item to list
_userages.append(99)
print(_userages)

#Deleting item from list
del _userages[1]
print(_userages)
