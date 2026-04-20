'''8. Write a Python program to find all numbers divisible by a given number k in a list using a function.
•	Accept a list of integers and k from the user. 
•	Create a function that returns a list of numbers divisible by k. 
•	Display the result.
'''
def find_div(numbers, k):
    result = []
    for num in numbers:
        if num % k ==0:
            result.append(num)
    return result
numbers = list(map(int, input("Enter the input: ").split()))
k = int(input("Enter value of k: "))
print("Numbers divisible by", k, "are")
print(find_div(numbers,k))