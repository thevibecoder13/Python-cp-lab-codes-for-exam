'''13. Write a Python program to find numbers in a list that have an even number of digits using a function.
•	Accept a list of integers from the user. 
•	Create a function that returns a list of numbers with even digits. 
•	Display the result.
'''
def even(l):
    even = []
    for num in l:
        if num % 2 == 0:
            even.append(num)
    return even
text = input("Enter: ")
lst = list(map(int, text.split()))
output = even(lst)
print("", output)