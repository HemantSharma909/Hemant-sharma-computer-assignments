def sorter():
    items=input("Enter string")
    j=items.split('-')

     
    j.sort()                                             
    print("alphabetically arranged words:")
    print('-'.join(j))


sorter()
