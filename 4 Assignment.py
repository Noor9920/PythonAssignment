string=input("Enter the String: ")
word=input("Enter a word: ")
word=word.lower()
string=string.lower().split('.')
l=0
count=0
for each in string:
    each=each.split()
    for each2 in each:
        l+=1
        if each2==word:
            count+=1

density=(count/l)
print('Density=',density)
