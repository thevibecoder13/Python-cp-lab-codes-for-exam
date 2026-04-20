'''7. Write a Python program to remove duplicate words from a sentence using a function.
•	Accept a sentence from the user. 
•	Create a function that returns the list without duplicates. 
•	Display the result.
'''
def remove_word(text):
    return list(set(text.lower().split()))
text = input("Enter the text: ")
print(" ".join(remove_word(text)))