'''15. Write a Python program to print the Fibonacci series up to the nth term using a recursive function.
•	The program should: 
o	Accept a positive integer n from the user. 
o	Use a recursive function to generate Fibonacci numbers. 
o	Display the Fibonacci series up to n terms. 
Note:
•	The Fibonacci series is defined as: 
o	F(0) = 0 
o	F(1) = 1 
o	F(n) = F(n−1) + F(n−2), for n ≥ 2 
'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
numb = int(input("Enter the input: "))
for i in range(numb):
    print(fibonacci(i), end=" ")