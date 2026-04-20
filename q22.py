'''
22. Write a Python program to count even and odd numbers in a list using a function.
•	Create a list of integers. 
•	Create a function that takes the list as input. 
•	Count even and odd numbers inside the function. 
•	Return both counts from the function. 
•	Display the results. 
'''
def count(text):
  even_count = 0
  odd_count = 0
  for num in text:
    if num % 2==0:
      even_count += 1
    else:
      odd_count +=1
  return even_count, odd_count
x = list(map(int, input("Enter nos: ").split()))
output = count(x)
print(output)
