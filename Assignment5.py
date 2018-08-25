L = ['Mango','Grapes','Mango','Apple','Grapes','Grapes']
word_list=[]
count_list=[]
L.sort()
for each in L:
    if each in word_list:
        pass
    else:
        word_list.append(each)
        count_list.append(L.count(each))
print(word_list)
print(count_list)
