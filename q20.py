'''def _sum(lst):
    summ = 0
    for i in range(len(lst)):
        summ += lst[i]
    return summ
text = input("Enter list elements: ")
lst = list(map(int, text.split()))
output = _sum(lst)
print("sum: ", output)'''
from functools import reduce
lst = list(map(int,input().split()))
output=reduce(lambda x,y: x+y,lst)
print(output)