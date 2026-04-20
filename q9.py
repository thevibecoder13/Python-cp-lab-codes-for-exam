'''9. Write a Python program to find the factorial of each number in a list using a higher order function.
•	Accept a list of non-negative integers. 
•	Create a function that returns a new list containing factorials of the original numbers. 
•	Display the result.
'''
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def factorial_list(numbers):
    return list(map(fact, numbers)) 
numbers = list(map(int, input("Enter non-negative integers (space-separated): ").split()))
result = factorial_list(numbers)
print("Factorials of the numbers are:")
print(result)