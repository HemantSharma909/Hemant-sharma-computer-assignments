#Q1)
print("Question 1")

x=int(input("Enter your marks to get your grade="))
if x<25:
    print("F grade")
elif x>=25 and x<=45:
    print("E grade")
elif x>=46 and x<=50:
    print("D grade")
elif x>=51 and x<=60:
    print("C grade")
elif x>=61 and x<=80:
    print("B grade")
elif x>=81 and x<=100:
    print("A grade")
print()
print("Question 2")

#Q2)

x=int(input("Enter the year you want to check weather it is a leap year or not="))

if x%100==0:
    if x%400==0:
        print('Leap year')
        
    else:
        print('Not a leap year')


  
elif x%4==0:
    print("Leap year")

else:
    print('Not a Leap year')

print()
print("Question 3")
print()

#Q3)

import random
from random import randint as r

for i in range(1,11):
    r1=r(1,20)
    r2=r(1,20)
    print("Question",i,":")
    print('Enter ',r1,'*',r2,':')
    result=int(input())
    if (result==r1*r2):
        print('True')
    else:
        print('False')
        print("The correct answer is",r1*r2)
print()
print("question 4")


#Q4)

x=int(input("Enter the number of candy you think are there in the jar="))
if x<=200:
    if x%5==2:
        if x%6==3:
            if x%7==2:
                print(x,"is the right guess about the candies present in the jar")
            else:
                print(x,"is not the right guess about the number of candies present in the jar")
        else:
            print(x,"is not the right guess about the number of candies present in the jar")
    else :
        print(x,"is not the right guess about the number of candies present in the jar")
else:
    print(x,"is not the right guess about the number of candies present in the jar")
