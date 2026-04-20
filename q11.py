'''11. Write a Python program to calculate the sum of even numbers in a list using a function.
•	Accept a list of integers from the user. 
•	Create a function that returns the sum of even numbers. 
•	Display the result.
'''
def sum_even(lst):
    add = 0
    for num in lst:
        if num % 2 == 0:
            add += num
    return add        

insert = input ("Add numbers: ")
lst = list(map(int,insert.split()))
result =   sum_even(lst)
print("sum: ", result)          