'''14.Write a Python program to find all pairs of numbers in a list whose sum equals a given number using a function.
•	Accept a list of integers and a target sum from the user. 
•	Create a function that returns a list of tuples, each representing a pair. 
•	Display the result.
'''
def sum(numbers, target):
    pair = []
    for i in range(len(numbers)):
        for j in range ( i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pair.append((numbers[i], numbers[j]))
    return pair
a = input("Enter numbers: ")
b = int(input("Enter the sum: "))
lst = list(map(int,a.split()))
output = sum(lst, b)
print("TUPLE: ", output)