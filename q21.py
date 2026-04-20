def max_min(min_max_lst):
    max = min_max_lst[0]
    min = min_max_lst[0]
    for i in range (len(min_max_lst)):
        if max < min_max_lst[i]:
            max = min_max_lst[i]
        elif min > min_max_lst[i]:
            min = min_max_lst[i]
    return max, min
a = list(map(int,input("Enter list of numbers: ").split()))
max_v, min_v = max_min(a)
print("Max: ", max_v, "Min: ", min_v)