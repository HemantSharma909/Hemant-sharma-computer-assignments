#Q.4
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"           
    for char in alphabet:
        if char not in str.lower():           
            return False                        
  
    return True
string = input("enter the string :")
if(ispangram(string)==True):
    print("yes, ",string, ", this string is Pangram")
else:
    print("No, ",string,", this string is not Pangram")
