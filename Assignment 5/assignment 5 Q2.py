# Question 2

x=int(input("Enter the smallest no. of the range="))
y=int(input("enter the largest no. of the range="))
z=int(input("enter the no you want to divide the particular range with="))
for i in range(x,y+1):
    if i%z==0:
        print(i)
