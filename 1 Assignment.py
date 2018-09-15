def takingInput():
    name=input("Enter the Name: ")
    roll_no=int(input("Enter the roll number: "))
    global subject
    subject=int(input("Enter the no of subjects: "))
    marks=[]
    for i in range(subject):
        marks.append(int(input("Enter the marks: ")))
    global total
    total=sum(marks)
def Percentage():
    takingInput()
    global percent
    percent=float(total/subject)
    print("Percentage is: ",percent)
    return percent
def Grade():
    Percentage()
    if percent>60:
        print("First Class")
    elif percent>40:
        print("Second Class")
    else:
        print("Fail")
    return 0
Grade()
