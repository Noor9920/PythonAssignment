n=input("Enter  the string")
a=n.isupper()
b=n.islower()
if a==True:
    print("The string is in upper case")
elif b==True:
    print("The String is in lower case")
else:
    print("The string contains both Upper and lower")
