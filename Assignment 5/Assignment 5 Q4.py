#Question 4
#To print the star pattern

no_of_rows=5
#Outer loop will print the number of rows
for i in range(0,no_of_rows):
    #Inner loop wil print the stars
    for j in range(0,i+1):
           print("* ",end='')
    #Changing line after each iteration
    print()

#For second pattern
for i in range(no_of_rows,0,-1):  
    for j in range(0,i-1):
        print("* ",end='')
    print()
