def remove_dup(lst):
    unique_lst = []
    for num in lst:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst
text = [1,1,2,3,3,4,5,6,6]
output = remove_dup(text)
print("", output)