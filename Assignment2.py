lst = []
num = int(input('How many numbers: '))
 
for each in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
 
print("Greatest no in the list is :", max(lst), "\nSmallest no in the list is :", min(lst))
