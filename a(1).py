'''
a = 3
print("a=", a, "type of", type(a))

a = 3.78
print("a=", a, "type of", type(a))

a = 3e-2 #3 * 10 ^ -2 = 3 * 2 / 100 = 0.03
print("a=", a, "type of", type(a))

a = 2-0.2j
print("a=", a, "type of", type(a))

a = "abc"
print("a=", a, "type of", type(a))

a = True
print("a=", a, "type of", type(a))

'''

'''

a, b = 3, 6
c = a + b # int + int
print(c, type(c))

a, b = 3, 6.8
c = a + b # int + float --> float + float = float, automatic/implicit/system conversion 
print(c, type(c))

a, b = 3, 6.8
c = a + int(b) # int + int, --> int, forcefully/explicit/ user conversion
print(c, type(c)) # 3 + 6 = 9

'''

'''

#Arithmetic Operators

a,b = 13,7
print(a/b) #1.8
print(a//b) #1
print(a%b) #6

a,b = 3,4
print(a**b) # a raise b = 81

#Relational Operators : form condition : true or false

a,b,c = 9,0,9
print(a>b) # True
print(a>=b) # False
print(a>=c) # True
print(a==c) # True
print(a!=b) # True

'''

a,b = 10,20
print("a=", a, "b=", b) #a = 10, b = 20

a,b = b,a = 10,20 # a -b , b - a
print("a=", a, "b=", b) #a = 10, b = 20

s = "Pragyan"
print(s[5])
print(s[-5])
print(s[2:5])
print(s[2:7:2])