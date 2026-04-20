from functools import reduce
def max_num(lst):
    return reduce(lambda a,b: a if a>b else b,lst )
lst = list(map(int,input().split()))
output = max_num(lst)
print(output)