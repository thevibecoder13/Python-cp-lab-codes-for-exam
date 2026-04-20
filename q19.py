import random
original_list = []
for i in range(10):
    num = random.randint(1,10)
    original_list.append(num)
print("Elements of list: ", original_list[::])
print("First 5 elements: ", original_list[:5])
print("Last 5 elements: ", original_list[-5:])
print("Index 2 to 7 elements: ", original_list[2:8])

even_lst = []
for i in range(10):
    if i % 2 == 0:
        even_lst.append(original_list[i])
print("Even index elements: ", even_lst)