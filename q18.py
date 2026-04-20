import random
original_list = []
for i in range(10):
    num = random.randint(1,10)
    original_list.append(num)
cube_list = []
for num in original_list:
    cube_list.append(num ** 3)
print("Original list: ", original_list)
print("After cubing: ", cube_list)