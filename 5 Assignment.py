n=input("Enter the String: ")
n=n.lower()
n=n.split()
count=0
for each in n:
    if each=='and' or each=='is' or each=='are' or each=='to':
        count+=1
print("Counts of excluded words is: ",count)
