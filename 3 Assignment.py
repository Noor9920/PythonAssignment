d1={'a':1,'b':2,'c':3,'d':4,'e':5,'c':6}
d=sorted(d1,key=d1.get,reverse=True)
for each in d[:3]:
    print(each,end=' ')
