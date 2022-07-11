#Q.1
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
n=int(input("enter the number :"))
if perfect_number(n)== True:
    print(n,",this is perfect number")
else:
    print(n,",this is not a perfect number")


