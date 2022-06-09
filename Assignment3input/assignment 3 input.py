#1 A program to convert a number in it's binary equivalent.
num = int(input("Enter a number="))
binary_equivalent = bin(num)
print(binary_equivalent)
print( )
print("question 2")

#2 Interactive python calculator program to have output after using arithmetic operations like addition,substraction,division,multiplication
x=float(input("Enter first number="))
y=float(input("Enter second number="))
z=input("what do want to do? /for division,+ for addition,- for substraction,* for multiplication=")
if z=='/':
    print("Final output is=",x/y)
elif z=='+':
    print("Final output is=",x+y)
elif z=='-':
    print("Final output is=",x-y)
elif z=='*':
    print("Final output is=",x*y)
print( )
print("question 3")

#3
import math

n = 10
r = 10
a = 10
b = 10
y2 = 20
y1 = 10
x2 = 30
x1 = 10

exp1 = (3+4) * (5)
exp2 = ((n)*(n-1)) / 2
exp3 = 4*(math.pi) * (math.pow(r,2))
exp4 = math.sqrt(r*(math.pow(math.cos(a), 2)) + r*(math.pow(math.sin(b), 2)))
exp5 = (y2 - y1)/(x2 - x1)

print(exp1)
print(exp2)
print(exp3)
print(exp4)
print(exp5)
print( )
print("question 4")

#4 The sequence of numbers that would be generated when the respective range is given.

for i in range(5):
    print(i, end=" ")
print()

for i in range(3,10):
    print(i, end=" ")
print()

for i in range(4,13,3):
    print(i, end=" ")
print()

for i in range(15,5,-2):
    print(i, end=" ")
print()

for i in range(5,3):
    print(i, end=" ")
print( )
print("question 5")

#5 The molecular weight of the carbohydrate based on the number of hydrogen,oxygen,carbon will be:-
    
Molecular_weight_of_Hydrogen=1.00794
Molecular_weight_of_Carbon=12.0107
Molecular_weight_of_Oxygen=15.9994
X=int(input("Enter the number of hydrogen atoms="))
Y=int(input("Enter the number of carbon atoms="))
Z=int(input("Enter the number of oxygen atoms="))
Molecular_weight_of_the_carbohydrate=X*1.00794 +Y*12.0107+Z*15.9994
print("Molecular weight of the carbohydrate is=",Molecular_weight_of_the_carbohydrate,"grams/mole")



