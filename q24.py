def sq(num_lst):
    squ = []
    for num in num_lst:
        squ.append(num * num)
    return squ
a = input("Enter a list of numbers: ")
lst = list(map(int, a.split()))
output = sq(lst)
print("", output)