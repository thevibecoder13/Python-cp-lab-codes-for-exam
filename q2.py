'''
2. Write a Python program to find all palindrome numbers in a list using a function.
•	Accept a list of integers from the user. 
•	Create a function that returns a list of palindrome numbers. 
•	Display the result.
'''
def is_pal(n):
     return str(n)==str(n)[::-1]
def find_pal(lst):
     return[n for n in lst if is_pal(n)]
num = list(map(int,input("Enter numbers: ").split()))
result = find_pal(num)
print("", result)