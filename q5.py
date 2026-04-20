'''5. Write a Python program to generate all prime factors of a number using a function.
•	Accept a number from the user. 
•	Create a function that returns a list of its prime factors. 
•	Display the result.
'''
def prime_factors(n):
    factors = []
    
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    
    return factors
num = int(input("Enter a number: "))
print("Prime factors:", prime_factors(num))