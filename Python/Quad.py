# Solve the quadratic equation ax**2 + bx + c = 0

# import math
import math
def myfunction(a,b,c):
    print(a)
    print(b)
    print(c)
    return("stuff")

returnedStuff = myFunction("hi",9,3334)

print(returnedStuff)

#To take coefficient input from the users
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

#calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-math.sqrt(d))/(2*a)
sol2= (-b+math.sqrt(d))/(2*a)

print('The solution are {0} and {1}'. format(sol1,sol2))


