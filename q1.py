'''
1.Write a Python program to remove all prime numbers from a list using a higher order function.
•	Accept a list of integers from the user. 
•	Create a function that returns a list with all prime numbers removed. 
•	Display the result.
'''
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def remove_prime(lst):
    return list(filter(lambda x: not is_prime(x), lst))

num = list(map(int,input("Enter numbers: ").split()))
result = remove_prime(num)
print("", result)