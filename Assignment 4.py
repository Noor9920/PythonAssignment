n=input("Enter the Name ")
c=input("Enter Contact no. ")
if (len(n)>=3 and len(n)<20) and n.isalpha():
    print("The entered name is correct")
    if c.isdigit() and len(c)==10:
        print("The Entered No is Correct")
    else:
        print("Entered contact no is incorrect Re-Enter")
else:
    print("Entered Name or contact no is incorrect Re-Enter")
