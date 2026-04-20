'''17. Write a Python program to check whether a person is eligible to vote or not using a function.
•	The program should: 
o	Accept the age of the user as input. 
o	Create a function that takes age as a parameter. 
o	Determine whether the age is greater than or equal to 18. 
o	Display an appropriate message: 
	“Eligible to vote” if age ≥ 18 
	“Not eligible to vote” if age < 18
'''
def vote(n):
    if n < 18:
        return "Not eligible to vote"
    else:
        return "Eligible to vote"
a = int(input("Enter age: "))
output = vote(a)
print("", output)