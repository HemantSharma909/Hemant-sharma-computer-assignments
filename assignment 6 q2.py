#Q.2
i=input("Enter str: ")
def palindrom(i) :  
    
    k=i.split(' ')
    n=''
    for p in k:
        n=n+p
    if n==n[::-1]:
        print("Palindrom")

    else:
        print('Not Palindrom')    
