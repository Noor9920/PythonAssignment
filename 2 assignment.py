string=input("Enter the string: ")
word=input("Enter the word: ")
word=word.lower()
count=0
string=string.lower().split('.')
for each in string:
    each=each.split()
    for check in each:
        if check==word:
            count+=1
print(word,":",count)
